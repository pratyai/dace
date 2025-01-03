import json
from pathlib import Path
from typing import List, Union, Any, Dict, Optional

from dace.frontend.fortran.ast_desugaring import ConstTypeInjection, ConstInstanceInjection, ConstInjection, SPEC
from dace.frontend.fortran.ast_internal_classes import BinOp_Node, Bool_Literal_Node, Call_Expr_Node, \
    Double_Literal_Node, Char_Literal_Node, Name_Node, Int_Literal_Node, Data_Ref_Node, Array_Subscript_Node, UnOp_Node

PROPAGATED_CONFIGS = """
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "use_aerosols", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_lw_cloud_scattering", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "use_general_cloud_optics", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_3d_effects", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_cloud_aerosol_per_lw_g_point", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_cloud_aerosol_per_sw_g_point", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_setup_ifsrrtm", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "use_spectral_solar_scaling", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_lw", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_sw", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_clear", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_sw_direct", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_lw_aerosol_scattering", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "use_beta_overlap", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "iverbosesetup", "value": "0"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "iverbose", "value": "0"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_weighted_surface_mapping", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_surface_sw_spectral_flux", "value": "true"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_fu_lw_ice_optics_bug", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_sw_delta_scaling_with_gases", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "cloud_fraction_threshold", "value": "1.0e-6"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "cloud_mixing_ratio_threshold", "value": "1.0e-9"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "cloud_inhom_decorr_scaling", "value": "0.5"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "min_gas_od_lw", "value": "1.0e-15"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "min_gas_od_sw", "value": "0.0"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "max_cloud_od", "value": "20.0"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "do_save_radiative_properties", "value": "false"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_overlap_scheme", "value": "1"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_solver_sw", "value": "2"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_solver_lw", "value": "2"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_gas_model_sw", "value": "1"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_gas_model_lw", "value": "1"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_liq_model", "value": "1"}
{"type": "ConstTypeInjection", "scope": null, "root": "radiation_config.config_type", "component": "i_ice_model", "value": "1"}
{"type": "ConstInstanceInjection", "scope": null, "root": "ecradhook.lhook", "component": null, "value": "false"}
"""


def generate_propagation_info(prop_info: List[Any]) -> Dict[str, str]:
    NUMERICAL_LITERALS = Union[Int_Literal_Node, Bool_Literal_Node, Double_Literal_Node]
    NOT_NUMERICAL_LITERALS = Union[BinOp_Node, Call_Expr_Node, Char_Literal_Node, Name_Node]

    def _key(_k: Union[Name_Node, Data_Ref_Node]) -> str:
        assert isinstance(_k, (Name_Node, Data_Ref_Node))
        if isinstance(_k, Name_Node):
            return _k.name.lower()
        elif isinstance(_k, Data_Ref_Node):
            return f"{_k.parent_ref.name}%{_k.part_ref.name}"

    # Seed values (imported from another module + populated with literals).
    seed_values: Dict[str, str] = {'iradaeroconst': '2', 'islope_rad': '0', 'ioverlapexponentialrandom': '1',
                                   'isolvermcica': '2', 'igasmodelifsrrtmg': '1', 'iliquidmodelsocrates': '1',
                                   'iicemodelfu': '1'}
    numerical_configs: Dict[str, str] = {k: v for k, v in seed_values.items()}
    for k, v in prop_info:
        if isinstance(k, (Name_Node, Data_Ref_Node)):
            assert _key(k)
            if isinstance(v, NUMERICAL_LITERALS):
                numerical_configs[_key(k)] = v.value.lower()
            elif isinstance(v, UnOp_Node):
                op, lval = v.op, v.lval
                assert op == '-' and isinstance(lval, Int_Literal_Node)
                numerical_configs[_key(k)] = f"-{lval.value}".lower()
            elif isinstance(v, NOT_NUMERICAL_LITERALS):
                continue
            else:
                raise NotImplementedError(f"{k} => {v}/{type(v)} is not implemented yet")
        elif isinstance(k, Array_Subscript_Node):
            continue
        else:
            raise NotImplementedError(f"{k}/{type(k)} => {v}/{type(v)} is not implemented yet")
    changed = True
    while changed:
        changed = False
        for k, v in prop_info:
            if (not isinstance(k, (Name_Node, Data_Ref_Node))
                    or not isinstance(v, Name_Node)):
                continue
            k_name, v_name = _key(k), v.name.lower()
            if k_name in numerical_configs or v_name not in numerical_configs:
                continue
            numerical_configs[k_name] = numerical_configs[v_name]
            changed = True
    rest = [(k, v) for k, v in prop_info
            if isinstance(k, (Name_Node, Data_Ref_Node))
            and _key(k) not in numerical_configs
            and not isinstance(v, (Char_Literal_Node, Call_Expr_Node,
                                   BinOp_Node))]
    with open('/Users/pmz/Downloads/propagated_consts.txt', 'w') as f:
        f.write('\n'.join([f"{k} | {v}" for k, v in PROPAGATED_CONFIGS.items()]))
    assert not rest
    return {k: v for k, v in numerical_configs if k not in seed_values}


def serialize(x: ConstInjection) -> str:
    assert isinstance(x, ConstInjection)
    d: Dict[str, Any] = {'type': type(x).__name__,
                         'scope': '.'.join(x.scope_spec) if x.scope_spec else None,
                         'root': '.'.join(x.type_spec if isinstance(x, ConstTypeInjection) else x.root_spec),
                         'component': '.'.join(x.component_spec) if x.component_spec else None,
                         'value': x.value}
    return json.dumps(d)


def deserialize(s: str) -> ConstInjection:
    d = json.loads(s)
    assert d['type'] in {'ConstTypeInjection', 'ConstInstanceInjection'}
    scope = tuple(d['scope'].split('.')) if d['scope'] else None
    root = tuple(d['root'].split('.'))
    component = tuple(d['component'].split('.')) if d['component'] else None
    value = d['value']
    return ConstTypeInjection(scope, root, component, value) \
        if d['type'] == 'ConstTypeInjection' \
        else ConstInstanceInjection(scope, root, component, value)


def deserialse_v2(s: str,
                  typ: SPEC,
                  scope: Optional[SPEC] = None) -> List[ConstTypeInjection]:
    cfg = [tuple(ln.strip().split('=')) for ln in s.split('\n') if ln.strip()]
    cfg = [(k.strip(), v.strip()) for k, v in cfg]
    injs = []
    for k, v in cfg:
        kparts = tuple(k.split('.')[1:])  # Drop the first part that represents the type, but is not specific.
        if v == 'T':
            v = 'true'
        elif v == 'F':
            v = 'false'
        injs.append(ConstTypeInjection(scope, typ, kparts, v))
    return injs


def config_injection_list() -> List[ConstInjection]:
    cfgs = [l.strip() for l in PROPAGATED_CONFIGS.splitlines() if l.strip()]
    cfgs = [deserialize(l) for l in cfgs]
    return cfgs

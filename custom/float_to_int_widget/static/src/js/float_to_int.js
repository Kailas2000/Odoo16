/** @odoo-module **/
import { registry } from "@web/core/registry"
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useInputField } from "@web/views/fields/input_field_hook";
const { Component, useRef } = owl

export class FloatToInt extends Component{
    setup(){
        this.input_data = useRef("floatint")
    }
    UpdateFloat(e){
        let input_data = this.input_data.el.value
        let int_value = Math.round(input_data);
        this.props.update(int_value)
    }
}
FloatToInt.template = "Float_To_Int";
FloatToInt.props = {
    ...standardFieldProps,
    options: { type: Object, optional: true}
}
FloatToInt.supportedTypes = ["float"];
FloatToInt.extractProps = ({attrs}) => {
    return {options: attrs.options}
}
registry.category("fields").add("float_int", FloatToInt)
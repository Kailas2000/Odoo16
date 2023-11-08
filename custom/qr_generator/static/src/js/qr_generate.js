/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";
class SystrayIcon extends Component {
    setup() {
        super.setup(...arguments);
    }
    _onClick_generate() {
        var input_data = $('#data').val()
        var qrcode = new QRCode(self.$('#qrcode')[0], {
            text: input_data,
            width: 128,
            height: 128,
        });
    }
    _onClick_reset() {
        console.log('bbbbb')
        $('#qrcode').empty();
    }
}
SystrayIcon.template = "qr_icon";
export const systrayItem = { Component: SystrayIcon,};
registry.category("systray").add("SystrayIcon", systrayItem, { sequence: 1 });
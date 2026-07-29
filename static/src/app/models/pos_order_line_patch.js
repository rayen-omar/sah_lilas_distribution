/** @odoo-module */

import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";
import { patch } from "@web/core/utils/patch";

patch(PosOrderline.prototype, {
    setup(vals) {
        super.setup(...arguments);
        this.sah_uom_id = this.sah_uom_id || false; 
    },
    
    get_sah_uom() {
        if (this.sah_uom_id) {
            return this.models["uom.uom"].getAllBy("id")[this.sah_uom_id];
        }
        return this.product_id.uom_id;
    },

    getSahQtyUnit() {
        const uom = this.get_sah_uom();
        const baseUom = this.product_id.uom_id;
        if (uom && baseUom && uom.id !== baseUom.id) {
            return this.qty * (baseUom.factor / uom.factor);
        }
        return this.qty;
    },

    getSahPriceUnit() {
        const uom = this.get_sah_uom();
        const baseUom = this.product_id.uom_id;
        if (uom && baseUom && uom.id !== baseUom.id) {
            return this.price_unit * (uom.factor / baseUom.factor);
        }
        return this.price_unit;
    },

    getSahDisplayPriceUnit() {
        return this.env.utils.formatCurrency(this.getSahPriceUnit());
    },
    
    export_as_JSON() {
        const json = super.export_as_JSON(...arguments);
        json.sah_uom_id = this.sah_uom_id;
        return json;
    }
});

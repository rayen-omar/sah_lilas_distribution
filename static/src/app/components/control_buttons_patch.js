/** @odoo-module */

import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { SelectionPopup } from "@point_of_sale/app/components/popups/selection_popup/selection_popup";
import { patch } from "@web/core/utils/patch";
import { makeAwaitable } from "@point_of_sale/app/utils/make_awaitable_dialog";

patch(ControlButtons.prototype, {
    async clickUom() {
        const order = this.currentOrder;
        if (!order) return;
        const line = order.getSelectedOrderline();
        if (!line) return;

        const product = line.product_id;
        const baseUom = product.uom_id;
        
        // Find all UoMs with the same category
        const allUoms = this.pos.models["uom.uom"].getAll();
        const categoryUoms = allUoms.filter((uom) => uom.category_id.id === baseUom.category_id.id);

        const selectionList = categoryUoms.map((uom) => ({
            id: uom.id,
            label: uom.name,
            isSelected: line.get_sah_uom() && line.get_sah_uom().id === uom.id,
            item: uom,
        }));

        const selectedUom = await makeAwaitable(this.dialog, SelectionPopup, {
            title: "Sélectionnez l'Unité",
            list: selectionList,
        });

        if (selectedUom) {
            line.sah_uom_id = selectedUom.id;
            
            // Adjust the price based on the UoM factor
            if (selectedUom.id !== baseUom.id) {
                const ratio = baseUom.factor / selectedUom.factor;
                line.set_unit_price(product.lst_price * ratio);
            } else {
                line.set_unit_price(product.lst_price);
            }
        }
    }
});

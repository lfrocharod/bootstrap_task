odoo.define('website_widget.website_widget', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    var MyWidget = publicWidget.Widget.extend({
        selector: '.o_portal_my_widget',
        events: {
            'click button': '_onClickButton',
        },

        start: function () {
            this._super.apply(this, arguments);
            this.$button = this.$('button');
        },

        _onClickButton: function () {
        console.log('Button clicked!');
            //if (this.$button) {
                this.$button.text('Thx!');
            /*} else {
                console.error('Button element not found.');
            }*/
        },
    });

    publicWidget.registry.MyWidget = MyWidget;

    return {
        MyWidget: MyWidget,
    };
});

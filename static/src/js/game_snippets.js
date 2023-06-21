odoo.define('website_game.website_game_dashboard', function(require){
    'use strict';
    var Animation = require('website.content.snippets.animation');
    var ajax = require('web.ajax');

    Animation.registry.get_dashbaord_carousel = Animation.Class.extend({
        selector : '.s_flappy_bird',
        init: function() {
            this._super.apply(this, arguments);
            console.log("Init loaded");
        },
        start: function(){
            console.log("Test");
            var self = this;
            ajax.jsonRpc('/get_dashbaord_carousel', 'call', {})
            .then(function (data) {
                if(data){
                    self.$target.empty().append(data);
                }
            });
        }
    });

    // Animation.registry.get_dashbaord_carousel = Animation.Class.extend({
    //     selector : '.s_jumper',
    //     init: function() {
    //         this._super.apply(this, arguments);
    //         console.log("Init loaded");
    //     },
    //     start: function(){
    //         console.log("Test");
    //         var self = this;
    //         ajax.jsonRpc('/get_dashbaord_carousel', 'call', {})
    //         .then(function (data) {
    //             if(data){
    //                 self.$target.empty().append(data);
    //             }
    //         });
    //     }
    // });

});
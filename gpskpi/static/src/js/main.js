odoo.define('gpskpi.kpi', function (require) {
    "use strict";

    var ControlPanelMixin = require('web.ControlPanelMixin');
    var AbstractAction = require('web.AbstractAction');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');
    var view_dialogs = require('web.view_dialogs');
    var core = require('web.core');
    var session = require('web.session');
    var _t = core._t;
    var ajax = require('web.ajax');

    var GPSKPI = AbstractAction.extend(ControlPanelMixin, {
        title: core._t('GPS KPI'),
        template: 'GPSKpi',

        init: function (parent, params) {
            this._super.apply(this, arguments);
            var self = this;
            this.action_manager = parent;
            this.params = params;
            this.startDate = false;
            this.endDate = false;
        },

        events: {
            'change .top_items_sales_w_m_y': 'get_crm_stages',
            'change .crm_won_status_w_m_y': 'get_crm_won_status',
            },

        start: function () {
            this._super.apply(this, arguments);
            this.set("title", this.title);
            this.update_control_panel({search_view_hidden: true}, {clear: true});
        },

        
        get_crm_stages : function(company_id){
            var self = this;
            var option = $(".top_items_sales_w_m_y option:selected").attr('data-value')
            if (!Number.isInteger(company_id)){
                company_id = self.$el.find('.pos-company option:selected').attr('data-id')
            }
            if(!option){
                option = 'month'
            }
            var start = moment().startOf(option).locale('en').format('YYYY-MM-DD');
            var end = moment().endOf(option).locale('en').format('YYYY-MM-DD');

            rpc.query({
                model: 'crm.lead',
                method: 'get_crm_stages1',
                args : [start, end, company_id]
            }, {async: false}).then(function (result) {
                if(result){
                    var contents = self.$el.find('.top_items_sold');
                    contents.empty();
                    var res = result
                    console.log("resdjhfjjjjjjjjjjjkdj", res)
                    var myTable= "<table style='margin-top: 15px;font-family:Trebuchet MS, Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;'>";
                    myTable+= "<tr><td colspan='4' style='padding-top: 12px; padding-bottom: 12px;text-align: center;background-color: #FFD733;border: 1px solid #ddd;padding: 8px;'>OPERACIONES</td></tr>";
                    myTable+= "<tr><td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>EN PROCESO</td>";
                    myTable+= "<td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>CON FECHA DE RATIFICACIÓN</td>";
                    myTable+= "<td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>CON FECHA DE COLOCACIÓN</td>";
                    myTable+= "<td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>RATIF, SIN FECHA DE COL</td></tr>";
                    console.log("iiiiiiiiiiiiiiiiii", res.en_proceso)
                    myTable+="<tr><td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>"+ res.en_proceso+"</td>";
                    myTable+="<td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>" + res.ratification+ "</td>";
                    myTable+="<td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>" + res.colocacion+ "</td>";
                    myTable+="<td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>" + res.ratificado+ "</td></tr>";  
                    myTable+="</table>";
                    self.$el.find('.top_items_sold').html(myTable)
                }
            });
        },

        get_crm_won_status : function(company_id){
            var self = this;
            var option = $(".crm_won_status_w_m_y option:selected").attr('data-value')
            if (!Number.isInteger(company_id)){
                company_id = self.$el.find('.pos-company option:selected').attr('data-id')
            }
            if(!option){
                option = 'month'
            }
            var start = moment().startOf(option).locale('en').format('YYYY-MM-DD');
            var end = moment().endOf(option).locale('en').format('YYYY-MM-DD');

            rpc.query({
                model: 'crm.lead',
                method: 'get_crm_won_status1',
                args : [start, end, company_id]
            }, {async: false}).then(function (result) {
                if(result){
                    var contents = self.$el.find('.crm_won_status');
                    contents.empty();
                    var res = result
                    console.log("crmwonstatussssssssssss", res)
                    var myTable= "<table style='margin-top: 15px;font-family:Trebuchet MS, Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;'>";
                    myTable+= "<tr><td colspan='3' style='padding-top: 12px; padding-bottom: 12px;text-align: center;background-color: #FFD733;border: 1px solid #ddd;padding: 8px;'>Sales</td></tr>";
                    myTable+= "<tr><td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>NEW</td>";
                    myTable+= "<td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>WON</td>";
                    myTable+= "<td style='text-align: center;border: 1px solid #ddd;padding: 8px;'>TO REACH THE GOAL</td></tr>";
                    myTable+="<tr><td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>"+ res.new+"</td>";
                    myTable+="<td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>"+ res.won+"</td>";
                    myTable+="<td style='text-align: center;border: 1px solid #ddd; padding: 8px;'>"+ res.goal+"</td></tr>";
                    myTable+="</table>";
                    self.$el.find('.crm_won_status').html(myTable)
                }
            });
        },


        renderElement: function () {
            var self = this;
            this._super.apply(this, arguments);
            var month = moment().month() + 1
        //     var week = moment().isoWeek()
        //     var temp = self.$el.find('.week-option');
        //     self.$el.find('.month-option option[value='+String(month)+']').attr('selected', 'selected');
        //     self.$el.find('.week-option option[value='+String(week)+']').attr('selected', 'selected');
        //     const firstDayOfMonth = moment(String(moment().year())+'-'+month+"'", 'YYYY-MM-DD');
        //     const numOfDays = firstDayOfMonth.daysInMonth();
        //     let weeks = new Set();
        //     for(let i = 0; i < numOfDays; i++){
        //         const currentDay = moment(firstDayOfMonth, 'YYYY-MM-DD').add(i, 'days');
        //         weeks.add(currentDay.isoWeek());
        //     }
        //     temp.empty();

        //     var res = Array.from(weeks)
        //     for(var i=0; i<res.length; i++){
        //         if(res[i] ==week || res[i] > week){
        //             temp.append('<option selected="selected" value="' + res[i] + '" data-id="'+ res[i]+'" >' + 'Week-'+res[i]+ '</option>');
        //             break
        //         }else if(res[i] > week){
        //             break
        //         }
        //         temp.append('<option value="' + res[i] + '" data-id="'+ res[i]+'" >' + 'Week-'+res[i]+ '</option>');
        //     }

        //     rpc.query({
        //         model: 'pos.session',
        //         method: 'getCompany',
        //     }, {async: false}).then(function (res) {
        //         if(res){
        //             $.each(res['company'], function(key, value) {
        //                 if(res['company_id'] === value['id']){
        //                         self.$el.find('.pos-company').append('<option selected="selected" value="' + value['company'] + '" data-id="'+ value['id']+'" >' + value['company'] + '</option>');
        //                 }else{
        //                     self.$el.find('.pos-company').append('<option value="' + value['company'] + '" data-id="'+ value['id']+'" >' + value['company'] + '</option>');
        //                 }
        //             });
        //         }
        //     });

            setTimeout(function(){
                // self.header_data();
                // self.filter_by_d_m_y('', '');
                
                self.get_crm_stages()
                self.get_crm_won_status();
               
            },0)
        },
    });
    core.action_registry.add('tag_kpi', GPSKPI);
    return {
        GPSKPI : GPSKPI,
    };
});

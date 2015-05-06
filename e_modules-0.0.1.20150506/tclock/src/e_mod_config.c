#include <e.h>
#include "e_mod_main.h"

struct _E_Config_Dialog_Data
{
   Eina_Bool show_time, show_date, show_tip;
   Evas_Object *time_entry, *date_entry, *tip_entry;
   const char *time_format, *date_format, *tip_format;
};

/* Protos */
static void *_create_data(E_Config_Dialog *cfd);
static void _free_data(E_Config_Dialog *cfd EINA_UNUSED, E_Config_Dialog_Data *cfdata);
static Evas_Object *_basic_create(E_Config_Dialog *cfd EINA_UNUSED, Evas *evas, E_Config_Dialog_Data *cfdata);
static int _basic_apply(E_Config_Dialog *cfd, E_Config_Dialog_Data *cfdata);

static void
_cb_changed(void *data, Evas_Object *obj EINA_UNUSED, void *event EINA_UNUSED)
{
   e_config_dialog_changed_set(data, EINA_TRUE);
}

static void
_cb_time_check_changed(void *data, Evas_Object *obj EINA_UNUSED, void *event EINA_UNUSED)
{
   E_Config_Dialog_Data *cfdata = ((E_Config_Dialog *)data)->cfdata;
   elm_widget_disabled_set(cfdata->time_entry, !cfdata->show_time);
   e_config_dialog_changed_set(data, EINA_TRUE);
}

static void
_cb_date_check_changed(void *data, Evas_Object *obj EINA_UNUSED, void *event EINA_UNUSED)
{
   E_Config_Dialog_Data *cfdata = ((E_Config_Dialog *)data)->cfdata;
   elm_widget_disabled_set(cfdata->date_entry, !cfdata->show_date);
   e_config_dialog_changed_set(data, EINA_TRUE);
}

static void
_cb_tip_check_changed(void *data, Evas_Object *obj EINA_UNUSED, void *event EINA_UNUSED)
{
   E_Config_Dialog_Data *cfdata = ((E_Config_Dialog *)data)->cfdata;
   elm_widget_disabled_set(cfdata->tip_entry, !cfdata->show_tip);
   e_config_dialog_changed_set(data, EINA_TRUE);
}

void
_config_tclock_module(Config_Item *ci)
{
   E_Config_Dialog *cfd = NULL;
   E_Config_Dialog_View *v = NULL;
   char buf[PATH_MAX];

   if (e_config_dialog_find("TClock", "_e_modules_tclock_config_dialog"))
     return;

   v = E_NEW(E_Config_Dialog_View, 1);
   v->create_cfdata = _create_data;
   v->free_cfdata = _free_data;
   v->basic.apply_cfdata = _basic_apply;
   v->basic.create_widgets = _basic_create;

   snprintf(buf, sizeof(buf), "%s/e-module-tclock.edj",
            tclock_config->mod_dir);

   tclock_config->cfd = e_config_dialog_new(NULL, D_("Tclock Settings"),
                                            "TClock",
                                            "_e_modules_tclock_config_dialog",
                                            buf, 0, v, ci);
}

static void
_fill_data(Config_Item *ci, E_Config_Dialog_Data *cfdata)
{
   cfdata->show_time = ci->show_time;
   cfdata->show_date = ci->show_date;
   cfdata->show_tip  = ci->show_tip;
   cfdata->time_format = eina_stringshare_ref(ci->time_format);
   cfdata->date_format = eina_stringshare_ref(ci->date_format);
   cfdata->tip_format  = eina_stringshare_ref(ci->tip_format);
}

static void *
_create_data(E_Config_Dialog *cfd)
{
   E_Config_Dialog_Data *cfdata = NULL;
   Config_Item *ci = NULL;

   ci = cfd->data;
   cfdata = E_NEW(E_Config_Dialog_Data, 1);
   _fill_data(ci, cfdata);
   return cfdata;
}

static void
_free_data(E_Config_Dialog *cfd EINA_UNUSED, E_Config_Dialog_Data *cfdata)
{
   if (!tclock_config) return;
   tclock_config->cfd = NULL;
   eina_stringshare_del(cfdata->time_format);
   eina_stringshare_del(cfdata->date_format);
   eina_stringshare_del(cfdata->tip_format);
   E_FREE(cfdata);
}

static Evas_Object *
_basic_create(E_Config_Dialog *cfd, Evas *evas, E_Config_Dialog_Data *cfdata)
{
   Evas_Object *o = NULL, *of = NULL, *obx = NULL, *bx = NULL;
   Evas_Object *time_entry = NULL, *time_check = NULL;
   Evas_Object *date_entry = NULL, *date_check = NULL;
   Evas_Object *tooltip_entry = NULL, *tooltip_check = NULL;

   Evas_Object *win = cfd->dia->win;

   o = elm_box_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   evas_object_show(o);
   bx = o;

   o = elm_frame_add(win);
   elm_object_text_set(o, D_("Top"));
   elm_frame_autocollapse_set(o, EINA_TRUE);
   elm_box_pack_end(bx, o);
   evas_object_show(o);
   of = o;

   o = elm_box_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_content_set(of, o);
   evas_object_show(o);
   obx = o;

   o = elm_check_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, D_("Show Top Line"));
   elm_check_state_pointer_set(o, &cfdata->show_time);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   time_check = o;

   o = elm_entry_add(win);
   elm_entry_scrollable_set(o, EINA_TRUE);
   elm_entry_single_line_set(o, EINA_TRUE);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, cfdata->time_format);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   time_entry = o;
   cfdata->time_entry = o;

   evas_object_smart_callback_add(time_check, "changed", _cb_time_check_changed, cfd);
   evas_object_smart_callback_add(time_entry, "changed", _cb_changed, cfd);
   elm_widget_disabled_set(time_entry, !cfdata->show_time);

   o = elm_label_add(win);
   elm_object_text_set(o, D_("Consult strftime(3) for format syntax"));
   elm_box_pack_end(obx, o);
   evas_object_show(o);

   o = elm_frame_add(win);
   elm_object_text_set(o, D_("Bottom"));
   elm_frame_autocollapse_set(o, EINA_TRUE);
   elm_box_pack_end(bx, o);
   evas_object_show(o);
   of = o;

   o = elm_box_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_content_set(of, o);
   evas_object_show(o);
   obx = o;

   o = elm_check_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, D_("Show Bottom Line"));
   elm_check_state_pointer_set(o, &cfdata->show_date);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   date_check = o;

   o = elm_entry_add(win);
   elm_entry_scrollable_set(o, EINA_TRUE);
   elm_entry_single_line_set(o, EINA_TRUE);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, cfdata->date_format);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   date_entry = o;
   cfdata->date_entry = o;

   evas_object_smart_callback_add(date_check, "changed", _cb_date_check_changed, cfd);
   evas_object_smart_callback_add(date_entry, "changed", _cb_changed, cfd);
   elm_widget_disabled_set(date_entry, !cfdata->show_date);

   o = elm_label_add(win);
   elm_object_text_set(o, D_("Consult strftime(3) for format syntax"));
   elm_box_pack_end(obx, o);
   evas_object_show(o);

   o = elm_frame_add(win);
   elm_object_text_set(o, D_("Tool Tip"));
   elm_frame_autocollapse_set(o, EINA_TRUE);
   elm_box_pack_end(bx, o);
   evas_object_show(o);
   of = o;

   o = elm_box_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_content_set(of, o);
   evas_object_show(o);
   obx = o;

   o = elm_check_add(win);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, D_("Show Tooltip"));
   elm_check_state_pointer_set(o, &cfdata->show_tip);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   tooltip_check = o;

   o = elm_entry_add(win);
   elm_entry_scrollable_set(o, EINA_TRUE);
   elm_entry_single_line_set(o, EINA_TRUE);
   evas_object_size_hint_weight_set(o, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   evas_object_size_hint_align_set(o, EVAS_HINT_FILL, EVAS_HINT_FILL);
   elm_object_text_set(o, cfdata->tip_format);
   elm_box_pack_end(obx, o);
   evas_object_show(o);
   tooltip_entry = o;
   cfdata->tip_entry = o;

   evas_object_smart_callback_add(tooltip_check, "changed", _cb_tip_check_changed, cfd);
   evas_object_smart_callback_add(tooltip_entry, "changed", _cb_changed, cfd);
   elm_widget_disabled_set(tooltip_entry, !cfdata->show_tip);

   o = elm_label_add(win);
   elm_object_text_set(o, D_("Consult strftime(3) for format syntax"));
   elm_box_pack_end(obx, o);
   evas_object_show(o);

   return bx;
}

static int
_basic_apply(E_Config_Dialog *cfd, E_Config_Dialog_Data *cfdata)
{
   Config_Item *ci = NULL;

   ci = cfd->data;
   ci->show_date = cfdata->show_date;
   ci->show_time = cfdata->show_time;
   ci->show_tip = cfdata->show_tip;
   eina_stringshare_del(ci->time_format);
   ci->time_format = eina_stringshare_add(elm_object_text_get(cfdata->time_entry));
   eina_stringshare_del(ci->date_format);
   ci->date_format = eina_stringshare_add(elm_object_text_get(cfdata->date_entry));
   eina_stringshare_del(ci->tip_format);
   ci->tip_format = eina_stringshare_add(elm_object_text_get(cfdata->tip_entry));

   e_config_save_queue();

   _tclock_config_updated(ci);
   return 1;
}

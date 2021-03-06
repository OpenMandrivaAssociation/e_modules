#ifndef __UTILS_H__
#define __UTILS_H__

Evas_Object *elfe_utils_fdo_icon_add(Evas_Object *parent, const char *icon, int size);
const char *elfe_utils_fdo_icon_path_get(Efreet_Menu *menu, int size);

E_Gadcon_Client_Class *elfe_utils_gadcon_client_class_from_name(const char *name);

#endif /* __UTILS_H__ */

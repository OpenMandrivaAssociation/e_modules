#ifndef E_MOD_MAIN_H
#define E_MOD_MAIN_H

#ifdef ENABLE_NLS
# include <libintl.h>
# define D_(str) dgettext(PACKAGE, str)
# define DP_(str, str_p, n) dngettext(PACKAGE, str, str_p, n)
#else
# define bindtextdomain(domain,dir)
# define bind_textdomain_codeset(domain,codeset)
# define D_(str) (str)
# define DP_(str, str_p, n) (str_p)
#endif

#define N_(str) (str)

E_Config_Dialog *wp_conf_show(Evas_Object *parent EINA_UNUSED, const char *params EINA_UNUSED);
void wp_conf_hide(void);

/**
 * @addtogroup Optional_Conf
 * @{
 *
 * @defgroup Module_Conf_Wallpaper2 Wallpaper2 (Alternative Selector)
 *
 * More graphically appealing wallpaper selector. It is targeted at
 * mobile devices.
 *
 * @note under development and not recommended for use yet.
 *
 * @see Module_Conf_Theme
 * @}
 */
#endif

GITDATE=`grep -E -m 1 [0-9]{8} e_modules.spec | awk '{printf $3}'`
VERSION=`grep Version: e_modules.spec | awk '{printf $2}'`
HOME=`pwd`
mkdir e_modules-`echo "$VERSION.$GITDATE"`
cd e_modules-`echo "$VERSION.$GITDATE"`
git clone http://git.enlightenment.org/enlightenment/modules/alarm.git/
git clone http://git.enlightenment.org/enlightenment/modules/comp-scale.git/
git clone http://git.enlightenment.org/enlightenment/modules/cpu.git/
git clone http://git.enlightenment.org/enlightenment/modules/desksanity.git/
git clone http://git.enlightenment.org/enlightenment/modules/diskio.git/
git clone http://git.enlightenment.org/enlightenment/modules/edgar.git/
git clone http://git.enlightenment.org/enlightenment/modules/eenvader.fractal.git/
git clone http://git.enlightenment.org/enlightenment/modules/elev8.git/
git clone http://git.enlightenment.org/enlightenment/modules/elfe.git/
git clone http://git.enlightenment.org/enlightenment/modules/empris.git/
git clone http://git.enlightenment.org/enlightenment/modules/engage.git/
git clone http://git.enlightenment.org/enlightenment/modules/everything-places.git/
git clone http://git.enlightenment.org/enlightenment/modules/everything-websearch.git/
git clone http://git.enlightenment.org/enlightenment/modules/eweather.git/
git clone http://git.enlightenment.org/enlightenment/modules/forecasts.git/
git clone http://git.enlightenment.org/enlightenment/modules/mail.git/
git clone http://git.enlightenment.org/enlightenment/modules/mem.git/
git clone http://git.enlightenment.org/enlightenment/modules/moon.git/
git clone http://git.enlightenment.org/enlightenment/modules/mpdule.git/
git clone http://git.enlightenment.org/enlightenment/modules/net.git/
git clone http://git.enlightenment.org/enlightenment/modules/news.git/
git clone http://git.enlightenment.org/enlightenment/modules/packagekit.git/
git clone http://git.enlightenment.org/enlightenment/modules/penguins.git/
git clone http://git.enlightenment.org/enlightenment/modules/photo.git/
git clone http://git.enlightenment.org/enlightenment/modules/places.git/
git clone http://git.enlightenment.org/enlightenment/modules/share.git/
git clone http://git.enlightenment.org/enlightenment/modules/tclock.git/
git clone http://git.enlightenment.org/enlightenment/modules/wallpaper2.git/
git clone http://git.enlightenment.org/enlightenment/modules/wlan.git/
rm -rf ./*/.git
rm -f ./*/.gitignore
cd $HOME
tar cJvf e_modules-`echo "$VERSION.$GITDATE"`.tar.xz ./e_modules-`echo "$VERSION.$GITDATE"`/*
#/bin/rm -R e_modules-`echo $VERSION`.`echo $GITDATE`
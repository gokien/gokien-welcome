# Welcome screen for Gokien

## Packaging
The package contains only a python script so it's fine to quickly packaging by `dpkg -b`:

```bash
# Remove "installed size" from previous run (optional)
git checkout gokien-welcome/DEBIAN/control
# Count installed size and include that in DEBIAN/control
du -s gokien-welcome/usr | read size ignoreMe
echo "Installed-Size: $size" >> gokien-welcome/DEBIAN/control
# Calculate checksums
cd gokien-welcome
find usr -type f -printf 'usr/%P ' | xargs md5sum > DEBIAN/md5sums
# Final step: build the deb
cd ..
dpkg -b gokien-welcome
# Rename the package
version=`dpkg -f gokien-welcome.deb version`
arch=`dpkg -f gokien-welcome.deb architecture`
mv gokien-welcome.deb "gokien-welcome_$version_$arch.deb"
```

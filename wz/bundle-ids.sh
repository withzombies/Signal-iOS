#!/usr/bin/env sh

set -v
set -x
set -o pipefail

# Change all the bundle ids
git ls-files -z "*.m" "*.swift" "*.plist" "*.entitlements" "Scripts/*" "Makefile" "Signal.xcodeproj/project.pbxproj" | xargs -0 -n 1 -I '{}' gsed -i 's/org\.whispersystems/com.withzombies/g' '{}'

# Add the sandbox entitlements
/usr/libexec/PlistBuddy -c "Merge wz/Signal.entitlements" Signal/Signal.entitlements
/usr/libexec/PlistBuddy -c "Merge wz/Signal-AppStore.entitlements" Signal/Signal-AppStore.entitlements
/usr/libexec/PlistBuddy -c "Merge wz/SignalShareExtension.entitlements" SignalShareExtension/SignalShareExtension.entitlements
/usr/libexec/PlistBuddy -c "Merge wz/SignalShareExtension-AppStore.entitlements" SignalShareExtension/SignalShareExtension-AppStore.entitlements
/usr/libexec/PlistBuddy -c "Merge wz/SignalNSE.entitlements" SignalNSE/SignalNSE.entitlements
/usr/libexec/PlistBuddy -c "Merge wz/SignalNSE-AppStore.entitlements" SignalNSE/SignalNSE-AppStore.entitlements

# Remove merchant / apple pay entitlement
git ls-files "*.entitlements" | xargs -n 1 /usr/libexec/PlistBuddy -c 'Delete :com.apple.developer.in-app-payments'

git ls-files "*.entitlements" | xargs -n 1 /usr/libexec/PlistBuddy -c 'Delete :com.apple.developer.pushkit.unrestricted-voip'
git ls-files "*.entitlements" | xargs -n 1 /usr/libexec/PlistBuddy -c 'Delete :com.apple.developer.usernotifications.filtering'


# Set main app display name to 'Signal Catalyst'
/usr/libexec/PlistBuddy -c "Set :CFBundleDisplayName 'Signal Catalyst'" Signal/Signal-Info.plist

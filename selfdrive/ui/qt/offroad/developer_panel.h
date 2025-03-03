#pragma once

#include "selfdrive/ui/qt/offroad/settings.h"

class DeveloperPanel : public ListWidget {
  Q_OBJECT
public:
  explicit DeveloperPanel(SettingsWindow *parent);
  void showEvent(QShowEvent *event) override;

private:
  Params params;
  ParamControl* adbToggle;
  ParamControl* joystickToggle;
  ParamControl* longManeuverToggle;
  ParamControl* cydiaLongitudinalToggle;
  ParamControl* experimentalLongitudinalToggle;
  bool is_release;
  bool offroad = false;

private slots:
  void updateToggles(bool _offroad);
};

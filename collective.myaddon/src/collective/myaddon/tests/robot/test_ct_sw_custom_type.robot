# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.myaddon -t test_sw_custom_type.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.myaddon.testing.COLLECTIVE_MYADDON_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/collective/myaddon/tests/robot/test_sw_custom_type.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a sw_custom_type
  Given a logged-in site administrator
    and an add sw_custom_type form
   When I type 'My sw_custom_type' into the title field
    and I submit the form
   Then a sw_custom_type with the title 'My sw_custom_type' has been created

Scenario: As a site administrator I can view a sw_custom_type
  Given a logged-in site administrator
    and a sw_custom_type 'My sw_custom_type'
   When I go to the sw_custom_type view
   Then I can see the sw_custom_type title 'My sw_custom_type'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add sw_custom_type form
  Go To  ${PLONE_URL}/++add++sw_custom_type

a sw_custom_type 'My sw_custom_type'
  Create content  type=sw_custom_type  id=my-sw_custom_type  title=My sw_custom_type

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the sw_custom_type view
  Go To  ${PLONE_URL}/my-sw_custom_type
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a sw_custom_type with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the sw_custom_type title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

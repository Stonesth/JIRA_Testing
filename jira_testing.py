from Tools import tools_v000 as tools
from Topdesk import topdesk as t
from Jira import jira as j
import os
from os.path import dirname


# -12 for the name of this project JIRA_Testing
save_path = dirname(__file__)[ : -12]
propertiesFolder_path = save_path + "Properties"

t.incidentNumber = "I2008-00972"
j.sprint = "PNN-TOS-PI2020.3.2"

j.epic_link = tools.readProperty(propertiesFolder_path, 'Jira_testing', 'epic_link=')
j.save_path = tools.readProperty(propertiesFolder_path, 'Jira_testing', 'save_path=')

def connectToJIRA() :
    tools.driver.get('https://jira-test.atlassian.insim.biz/')


# Open Browser
tools.openBrowserChrome()

# TopDesk part
t.connectViaLink()
t.incidentTitle()

jiraTitle = t.incidentNumber + " - " + t.incidentTitle 
# Jira part
connectToJIRA()
j.createJira(jiraTitle, t.description_text, t.incidentNumber)

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Messages used in the dashboard."""

__author__ = 'Mike Gainer (mgainer@google.com)'


AVAILABILITY_AVAILABILITY_DESCRIPTION = """
Content defaults to the availability of the course, but may also be restricted
to admins (Private) or open to the public (Public).
"""

AVAILABILITY_SHOWN_WHEN_UNAVAILABLE_DESCRIPTION = """
If checked, the content displays its title in the syllabus even when it is
private.
"""

CONTENTS_OF_THE_COURSE_DESCRIPTION = """
The course.yaml file contains all course-level settings.  It can be
modified from other settings sub-tabs, or directly edited in its
raw form here.
"""

COURSE_TEMPLATE_DESCRIPTION = """
The course_template.yaml file provides default values for course settings.
These values are not dynamically editable, but you can override them
by editing your course.yaml file directly, or by changing settings in
the other Settings sub-tabs.

You can also change the default settings for all courses by editing
the course_template.yaml file on disk and re-pushing CourseBuilder to
AppEngine.  Changing the defaults in the file will not erase or
override any course-specific settings you may have made.
"""

EMBED_ASSESSMENT_DESCRIPTION = """
This link allows the assessment to be embedded in any web page.
"""

ENABLE_HOOK_EDITS = """
If checked, controls on course pages will be displayed to permit editing of HTML
inclusions (hook points). Otherwise, the course pages will appear as students
would see it.
"""

SHOW_JINJA_CONTEXT = """
If checked, a dump of Jinja context contents will be displayed at the bottom of
course pages (only for admins and only on the development server).
"""

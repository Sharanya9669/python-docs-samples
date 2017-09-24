# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


def convert_temp(cel_temp):
    ''' convert Celsius temperature to Fahrenheit temperature '''
    if cel_temp == "":
        return ""
    try:
        far_temp = float(cel_temp) * 9 / 5 + 32
        far_temp = round(far_temp, 3)  # round to three decimal places
        return str(far_temp)
    except ValueError:  # user entered non-numeric temperature
        return "invalid input"


class MainPage(webapp2.RequestHandler):
    def get(self):
        cel_temp = self.request.get("cel_temp")
        far_temp = convert_temp(cel_temp)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Temperature Converter</title></head>
            <body>
              <form action="/" method="get">
                Celsius temperature: <input type="text"
                                        name="cel_temp" value={}>
                <input type="submit" value="Convert"><br>
                Fahrenheit temperature: {}
              </form>
            </body>
          </html>""".format(cel_temp, far_temp))

routes = [('/', MainPage)]

my_app = webapp2.WSGIApplication(routes, debug=True)

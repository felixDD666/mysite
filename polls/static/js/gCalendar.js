 // Your Client ID can be retrieved from your project in the Google
      // Developer Console, https://console.developers.google.com
      var CLIENT_ID = '1010938660321-ts2ibcqj4phe4f59elgspj8mm9cpf65g.apps.googleusercontent.com';

      var SCOPES = ["https://www.googleapis.com/auth/calendar"];

      /**
       * Check if current user has authorized this application.
       */

      $( document ).ready(function() {
        $('#cuerpoCitas').css('display','none');
      });

      window.onload = function(){
        gapi.auth.authorize(
          {
            'client_id': CLIENT_ID,
            'scope': SCOPES.join(' '),
            'immediate': true
          }, handleAuthResult);
      }
      /*
      function checkAuth() {
        console.log("loadCalendar");
        gapi.auth.authorize(
          {
            'client_id': CLIENT_ID,
            'scope': SCOPES.join(' '),
            'immediate': true
          }, handleAuthResult);
      }
        */
      /**
       * Handle response from authorization server.
       *
       * @param {Object} authResult Authorization result.
       */
      function handleAuthResult(authResult){
        console.log(authResult)
        var authorizeDiv = document.getElementById('authorize-div');
        if (authResult && !authResult.error) {
          // Hide auth UI, then load client library.
          authorizeDiv.style.display = 'none';
          loadCalendarApi();
        } else {
          // Show auth UI, allowing the user to initiate authorization by
          // clicking authorize button.
          authorizeDiv.style.display = 'inline';
        }
        /*
        var access_token = authResult.access_token;
        var url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={ya29.CjCWA-VquPkAGL8LhFNlf6QI_jq3NGSl5JWomhALuuzJqCx9ad6vLTjR5jnEnrNdr90}';

          $.ajax({
            type: 'GET',
            url: url,
            async: false,
            success: function(userInfo) {
              //info about user
              console.log(userInfo);
              console.log('test');
            },
            error: function(e) {
              console.log('error');

            }
        });
        */
      }

      /**
       * Initiate auth flow in response to user clicking authorize button.
       *
       * @param {Event} event Button click event.
       */
      function handleAuthClick(event) {
        gapi.auth.authorize(
          {client_id: CLIENT_ID, scope: SCOPES, immediate: false},
          handleAuthResult);
        return false;
      }

      /**
       * Load Google Calendar client library. List upcoming events
       * once client library is loaded.
       */
      function loadCalendarApi() {
        $('#cuerpoCitas').css('display','block');
        gapi.client.load('calendar', 'v3', listUpcomingEvents);
      }

      /**
       * Print the summary and start datetime/date of the next ten events in
       * the authorized user's calendar. If no events are found an
       * appropriate message is printed.
       */
      function listUpcomingEvents() {
        var request = gapi.client.calendar.events.list({
          'calendarId': 'primary',
          'timeMin': (new Date()).toISOString(),
          'showDeleted': false,
          'singleEvents': true,
          'maxResults': 10,
          'orderBy': 'startTime'
        });

        request.execute(function(resp) {
          var events = resp.items;
          appendPre('Proximos Eventos:');
          if (events.length > 0) {
            for (i = 0; i < events.length; i++) {
              var event = events[i];
              var when = event.start.dateTime;
              if (!when) {
                when = event.start.date;
              }
              var when2 = event.end.dateTime;
              if (!when2) {
                when2 = event.end.date;
              }
              appendPre(event.summary + ' (' + when + ')-->' + ' (' + when2 + ')')
            }
          } else {
            appendPre('No upcoming events found.');
          }
        });
      }

      function clickCrearCita(){
        
        var event = {
          'summary': $('#summary').val(),
          'location': $('#where').val(),
          'start': {
            'date': $('#when1').val(),
          },
          'end': {
            'date': $('#when2').val(),
          }
        };
        var request = gapi.client.calendar.events.insert({
          'calendarId': 'primary',
          'resource': event
        });
        console.log("Request");

        request.execute(function(event) {
          appendPre('Event created: ' + event.htmlLink);
          console.log("Execute");
        });
        setTimeout(function(){ location.reload(); }, 1500);
      }


      
        /*
        
      */
      /**
       * Append a pre element to the body containing the given message
       * as its text node.
       *
       * @param {string} message Text to be placed in pre element.
       */
      function appendPre(message) {
        var pre = document.getElementById('output');
        var textContent = document.createTextNode(message + '\n');
        pre.appendChild(textContent);
      }
      
      
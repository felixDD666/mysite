var config = 
{
  "widgetUrl": "http://felixdd666.pythonanywhere.com/admin",
  "signInSuccessUrl": "http://felixdd666.pythonanywhere.com/admin",
  "signOutUrl": "http://felixdd666.pythonanywhere.com/admin",
  "oobActionUrl": "/",
  "apiKey": "",
  "siteName": "this site",
  "signInOptions": ["password","google"]
}

	window.google.identitytoolkit.start(
      '#gitkitWidgetDiv', // accepts any CSS selector
      config,
      '{{ POST_BODY }}');
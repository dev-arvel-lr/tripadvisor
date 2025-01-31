chrome.webRequest.onAuthRequired.addListener(
  function (details) {
    return {
      authCredentials: {
        username: "AbCdEf654321", // Replace with actual username
        password: "AbCdEf123456_country-jp", // Replace with actual password
      },
    };
  },
  { urls: ["<all_urls>"] }, // Match all URLs
  ["blocking"]
);

// Optional: Set up a proxy server if needed
chrome.proxy.settings.set(
  {
    value: {
      mode: "fixed_servers",
      rules: {
        singleProxy: {
          scheme: "http",
          host: "geo.iproyal.com", // Replace with actual proxy host
          port: 12321, // Replace with actual proxy port
        },
        bypassList: ["localhost", "127.0.0.1"],
      },
    },
    scope: "regular",
  },
  function () {}
);

const { Builder, By, Key, until } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");

async function attachToLocalChrome() {
  // Configure Chrome options to attach to the debugger
  const proxyAddress =
    "http://AbCdEf654321:AbCdEf123456_country-jp@geo.iproyal.com:12321";
  const options = new chrome.Options();
  options.addArguments(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    `proxy-server=${proxyAddress}`
  ); // Port used in the --remote-debugging-port flag

  // Attach to the existing Chrome instance
  let driver = new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  try {
    // Step 1: Navigate to Google
    // await driver.get("https://www.tripadvisor.com/CreateListing.html");
    await driver.get("https://whatismyipaddress.com/");
    // // Step 2: Find the search bar and perform a search
    // const searchBox = await driver.findElement(By.name("q"));
    // await searchBox.sendKeys("Selenium WebDriver Node.js", Key.RETURN);

    // // Step 3: Wait for the search results to load
    // await driver.wait(until.titleContains("Selenium WebDriver Node.js"), 5000);

    // // Step 4: Click the first result link
    // const firstResult = await driver.wait(
    //   until.elementLocated(By.css("h3")),
    //   5000
    // );
    // await firstResult.click();

    // Step 5: Print the new page's title
    await driver.wait(until.titleIs("Selenium WebDriver Node.js"), 50000); // Adjust title to the expected result
    console.log("New Page Title:", await driver.getTitle());
  } catch (error) {
    console.error("Error:", error);
  } finally {
    // Do not quit the browser; let the local instance remain open
    console.log("Script finished.");
  }
}

attachToLocalChrome();

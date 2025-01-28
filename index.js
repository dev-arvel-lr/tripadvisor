const { Builder, By, until, Browser, Key } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
(async function example() {
  // Initialize the WebDriver (use Chrome in this case)
  let options = new chrome.Options();
  options.addArguments("--disable-gpu"); // Disable GPU hardware acceleration

  let driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  try {
    // Open the website
    await driver.get("https://www.google.com/");

    // Wait for an element to be present (use 'id' to find the element)
    let searchBox = await driver.wait(
      until.elementLocated(By.xpath('//*[@id="APjFqb"]')),
      10000
    );

    // Type the search query
    await searchBox.sendKeys("Tripadvisor");

    // Press Enter to perform the search (you can also click the 'Google Search' button if preferred)
    await searchBox.sendKeys(Key.ENTER);

    // Wait for the first search result to be located (use CSS selector or XPath)
    let firstLink = await driver.wait(
      until.elementLocated(By.css("h3")),
      10000
    );

    // Click the first link (search result)
    await firstLink.click();

    // Capture the title of the page
    let title = await driver.getTitle();
    console.log(`Page title: ${title}`);
  } catch (error) {
    console.log("Error");
  }
})();

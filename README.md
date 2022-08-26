# Welook Moments Scraper
*Welook Moments Scraper* is a Python scraper for the Community Moments page of [POAPs](https://poap.xyz/) found at [Welook](https://welook.io/). It scrapes all the images uploaded to that POAP and save them at the `/images` folder.

You can see an example of a *POAP Community Moments* page [here](https://welook.io/moments/59601).

You can see a demo of this scraper working [here](https://youtu.be/YqNDohoeaFg).

Built using *Python*, *Selenium* and *Beautiful Soup 4*.

## Usage
1. Clone the repo
    ```
    git clone https://github.com/tadeodonegana/welook-moments-scraper.git
    ```
2. Install the required dependencies
    ```
    pip install -r requirements.txt
    ```
3. Create the `/images` and `/poap-img` folders
    ```
    mkdir images
    mkdir poap-img
    ```
4. Run the scraper
    ```
    python main.py --generate [MOMENTS_PAGE_URL]
    ```
## Example
Run the scraper using Python:
    ```
    python main.py --generate https://welook.io/moments/59601
    ```

Check the `/images` and `/poap-img` folders to see the results.
## Contributing 
PRs and issues are always welcome. Feel free to submit any issues you have at: [https://github.com/tadeodonegana/welook-moments-scraper/issues](https://github.com/tadeodonegana/welook-moments-scraper/issues)
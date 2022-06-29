{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "path = \"C:/Users/marwen/Desktop/MongoDB/chromedriver/chromedriver.exe\"\n",
    "website = \"https://www.thesun.co.uk/sport/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\marwen\\AppData\\Local\\Temp/ipykernel_12736/744449086.py:3: DeprecationWarning: executable_path has been deprecated, please pass in a Service object\n",
      "  driver = webdriver.Chrome(executable_path=path, options=options)\n"
     ]
    }
   ],
   "source": [
    "options = Options()\n",
    "options.headless= True\n",
    "driver = webdriver.Chrome(executable_path=path, options=options)\n",
    "driver.get(website)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "containers = driver.find_elements(by=\"xpath\" , value='//div[@class=\"teaser__copy-container\"]')\n",
    "titles = []\n",
    "subtitles = []\n",
    "links = []\n",
    "for container in containers:\n",
    "    title = container.find_element(by='xpath', value='./a/h2').text\n",
    "    subtitle = container.find_element(by='xpath', value='./a/p').text\n",
    "    link = container.find_element(by='xpath', value='./a').get_attribute(\"href\")\n",
    "    titles.append(title)\n",
    "    subtitles.append(subtitle)\n",
    "    links.append(link)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "Mydict = {'Titles': titles, 'Subtitles': subtitles, 'links': links}\n",
    "df = pd.DataFrame(Mydict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('C:/Users/marwen/Desktop/MongoDB/theSun.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.6 ('football')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "ab19c3871d25b514e360b1b20486996f28448ef9bc3dcd2a82ae3ca074b8dbcd"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

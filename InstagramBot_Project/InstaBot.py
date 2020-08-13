from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import datetime
import sys
import random


class InstagramBot:
    
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)  # wait to get to the log-in screen

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)  # wait for Instagram to log you in

    def followWithUsername(self, username):  # follow the specified user
        self.browser.get(username)
        time.sleep(2)  # not necessary

        try:
            followButton = self.browser.find_elements_by_css_selector('button')[0]

            if followButton.text != 'Message':  # if you are not following the user

                if followButton.text == 'Follow':
                    followButton.click()  # follow the user
                    print("followed public user: " + username)
                    time.sleep(2)  # wait after following the user
                else:
                    followButton = self.browser.find_elements_by_css_selector('button')[1]  # if private user
                    if followButton.text == 'Follow':
                        followButton.click()  # Follow the user
                        print("followed private user: " + username)
                        time.sleep(2)  # wait after following the user
                    else:
                        print("unknown error following user: " + username)
            else:
                print("Already following user: " + username)
        except IndexError:  # if the user doesn't exist
            print("This user doesn't exist: " + username)
            pass

    def unfollowWithUsername(self, username):
        self.browser.get(username)
        time.sleep(2)
        checkFollowButton = self.browser.find_element_by_css_selector('button')

        if checkFollowButton.text == 'Message':
            unfollowButton = self.browser.find_elements_by_css_selector('button')[1]
            unfollowButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following this user")

    def getUserFollowers(self, username, max_followers):  # get the followers of the specified user
        self.browser.get(username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(3)  # wait for followers list to load
        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
        print("Before = ", numberOfFollowersInList)
        followersList.click()

        actionChain = webdriver.ActionChains(self.browser)

        while (numberOfFollowersInList < max_followers):
            time.sleep(1)
            # actionChain.key_down(Keys.SPACE).perform()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

            try:
                numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
                time.sleep(1)
                followersList.click()
            except:
                print("1st exception hit!")
                self.closeBrowser()
                sys.exit()

            print("After = ", numberOfFollowersInList)

        followers = []
        try:
            for user in followersList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                print(userLink)
                followers.append(userLink)
                if len(followers) == max_followers:
                    break
        except:
            print("2nd exception hit!")
            self.closeBrowser()
            sys.exit()

        return followers

"""
    def getUserFollowers2(self, username, max):  # get the followers of the specified user
        self.browser.get(username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(3)  # wait for followers list to load

        followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')

        #numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        #print "Before = ", numberOfFollowersInList
        #followersList.click()

        #actionChain = webdriver.ActionChains(self.browser)

        # We need to scroll the followers modal to ensure that all followers are loaded
        while True:
            self.browser.execute_script("followersbox.scrollTo(0, followersbox.scrollHeight);")

            # Wait for page to load
            time.sleep(0.5)

            # Calculate new scrollHeight and compare with the previous
            new_height = self.browser.execute_script("return followersbox.scrollHeight;")
            if new_height == last_height:
                break
            last_height = new_height

        followers = []
        try:
            for user in followersList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute('href')
                print(userLink)
                followers.append(userLink)
                if len(followers) == max:
                    break
        except:
            print ("2nd exception hit!")
            self.closeBrowser()
            sys.exit()

        return followers
"""

    def CsvWrite(self, my_list, follower_csv):
        with open(follower_csv, mode='a+') as followers_file:
            followers_writer = csv.writer(followers_file, delimiter=',')
            # followers_writer.writerow(['Serial_no.,Followers User_link'])
            datetime_object = datetime.datetime.now()

            count = 0
            for i in my_list:
                count += 1
                followers_writer.writerow([count, i, datetime_object])

    def CsvRead(self):
        with open('mylist.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # print csv_reader
            for row in csv_reader:
                for i in row:
                    print(i + ",",)

    def closeBrowser(self):
        self.browser.close()

    # def followersOffollowers(self, max, follow):
    #
    #     for i in follow:
    #         self.getUserFollowers(i, max)
    #         time.sleep(2)
    #
    #         if i == max:
    #             break


if __name__ == "__main__":
    f = open("./account.txt", "r")
    lines = f.readlines()
    username = lines[0]
    password = lines[1]
    f.close()

    bot = InstagramBot(username, password)
    bot.signIn()

    SourceOfFame = "https://www.instagram.com/tomcruise/"
    follower_csv = 'followers_file.csv'

    user_list = [SourceOfFame]
    max_no_of_followers = 5
    follower_list = bot.getUserFollowers(SourceOfFame, max_no_of_followers)
    print(follower_list)

    bot.CsvWrite(follower_list, follower_csv)
    # bot.followWithUsername(user_list[0])
    for follower in follower_list:
        bot.followWithUsername(follower)
        ts = random.randint(2, 8)  # pick random time between 2-8 seconds
        time.sleep(ts)

    time.sleep(30)  # wait a little before closing browser
    bot.closeBrowser()

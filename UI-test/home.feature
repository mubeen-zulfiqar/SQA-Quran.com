Feature: Quran.com Home Page Assesment
    As a user of Quran.com
    I want to view all the contents properly And be able to easily access and navigate the website's home page.

    Background: On home page of Quran.com
    Given I am on the Quran.com home page
    
        Scenario: All Surah Tags are shown
            Then All the Surah tags are shown

        Scenario: View By Tab 
            Then View By Tab is present

        Scenario Outline: Viewing by Surah,Juz and Revelation   
        When I switch to "<tab>"     
        Then the "<view>" is switched

        Examples: Tabs
            | tab | view | 
            | Juz | JuzView_juzTitle__mVq8J |
            | Surah | SurahPreviewRow_container__3ZfRV | 
            | Revelation Order | ChapterAndJuzList_revelationOrderDisclaimer__ymzfy |

        Scenario: Logo Presence 
            Then The Logo is Present
        
        Scenario: Search by Voice 
            Then Search by Voice is Availabe  

        Scenario: Radio 
            Then Radio Play is Availabe  
            
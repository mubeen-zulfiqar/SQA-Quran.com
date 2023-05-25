Feature: Quran.com Surah Page Assesment
    As a user of Quran.com
    I want to view all the contents properly of SURAH page.

    Background: On Surah page of Quran.com
        Given I am on the Quran.com Surah page

        Scenario: Surah Name
        Then Surah Name is Present

        Scenario: Translator Name
        Then Translator Name is Present

        Scenario: Change Translator
        Then Change Translator is Availabe

        Scenario: Surah Info
        Then Surah Info is Present

        Scenario: Change Translator
        When I Press Change Translation Button
        Then The list of Translators is Given

        Scenario Outline: Viewing by Surah Translation or Reading   
        When I switch to "<tab>" in Surah Page     
        Then the "<view>" is switched in Surah Page

        Examples: Tabs
            | tab | view | 
            | //button[normalize-space()='Reading'] | //div[@id='page-1'] |
            | //button[normalize-space()='Translation'] | //div[@class='ChapterHeader_translationBy__DDZAE'] |
        
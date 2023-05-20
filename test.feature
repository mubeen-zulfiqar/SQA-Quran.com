Feature: Testing quran.com

  Scenario: Search for a specific verse
    Given I am on Quran.com
    When I search for "Surah Al-Fatiha, Verse 1"
    Then I should see the verse "In the name of Allah, the Entirely Merciful, the Especially Merciful."

  Scenario: Change the language of the Quran
    Given I am on Quran.com
    When I click on the language dropdown
    And I select "Urdu"
    Then the Quran text should be displayed in Urdu.

  Scenario: Bookmark a verse
    Given I am on Quran.com
    When I navigate to "Surah Al-Baqarah, Verse 255"
    And I click on the "Bookmark" button
    Then the verse should be saved to my bookmarks.

  Scenario: Share a verse on social media
    Given I am on Quran.com
    When I navigate to "Surah An-Nisa, Verse 36"
    And I click on the "Share" button
    And I select "Twitter"
    Then a tweet containing the verse should be composed and ready to post.

  Scenario: Listen to a recitation of the Quran
    Given I am on Quran.com
    When I navigate to "Surah Al-Fajr"
    And I click on the "Play" button
    Then a recitation of the chapter should begin playing.

  Scenario: Listen to a recitation of the Quran
    Given I have selected a surah
    When I click on the "Play" button
    And I click on the "Play" button
    Then a recitation of the chapter should begin playing.

  Scenario Outline: Scenario Outline name: Change the Translation of the Quran
    Given I am on Quran.com
    When I click on the translation dropdown
    And I select <reciter>
    Then the translation text should be displayed in <translator>'s transloation.

  Example: Change the Translation of the Quran
    | reciter | translator |
    | English | Muhammad Marmaduke Pickthall |
    | English | Abdullah Yusuf Ali |
    | English | Muhammad Sarwar |
    | Farsi | Saheeh International |
    | Farsi | Muhammad Marmaduke Pickthall |
    | Urdu | Nauman Ali Khan |

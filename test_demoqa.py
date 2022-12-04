import os
from selene.support.shared import browser
from selene import be, have


def test_practice_form(browser_open):
    # Заполняем данные
    browser.element('#firstName').should(be.blank).type('Andrew')
    browser.element('#lastName').should(be.blank).type('Chizh')
    browser.element('#userEmail').should(be.blank).type('andrechizh8@yandex.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('9183346139')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1992"]').click()
    browser.element('.react-datepicker__day--008').click()
    browser.element('#subjectsInput').type('Physic').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('D:/QA_GURU_HW/QA_GURU_hw_4/img/pepe.jpg'))
    browser.element('#currentAddress').type('Krasnodar,Shirokaia 53')
    browser.element('[id="react-select-3-input"]').type('Uttar Pradesh').press_enter()
    browser.element('[id="react-select-4-input"]').type('Agra').press_enter()
    browser.element('#submit').press_enter()
    # Проверяем данные
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Andrew Chizh',
        'andrechizh8@yandex.ru',
        'Male',
        '9183346139',
        '08 December,1992',
        'Physics',
        'Reading',
        'pepe.jpg',
        'Krasnodar,Shirokaia 53',
        'Uttar Pradesh Agra'))

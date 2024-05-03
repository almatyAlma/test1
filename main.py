browser.open('https://school.qa.guru')
browser.element('[name="email"]').type('alma.bekbergenova@tele2.kz').press_enter()
browser.element('[name="password"]').type('+5x++b++Y').press_enter().press_enter()
browser.element('[class="page-header"]').should(have.text('Оценка на ДЗ'))

browser.open('https://school.qa.guru/cms/system/login')
browser.element('[class="logined-form"]').should(have.text('Здравствуйте, Алма'))

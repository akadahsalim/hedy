import textwrap

from tests.Tester import HedyTester


class TestsLevel9(HedyTester):
    level = 9
    '''
    Tests should be ordered as follows:
     * commands in the order of hedy.py e.g. for level 1: ['print', 'ask', 'echo', 'turn', 'forward']
     * combined tests
     * markup tests
     * negative tests

    Naming conventions are like this:
     * single keyword positive tests are just keyword or keyword_special_case
     * multi keyword positive tests are keyword1_keywords_2
     * negative tests should be situation_gives_exception
    '''

    #
    # if nesting
    #
    def test_if_nested_in_if(self):
        code = textwrap.dedent("""\
        n is 1
        m is 2
        if n is 1
            if m is 2
                print 'great!'""")

        expected = textwrap.dedent("""\
        n = '1'
        m = '2'
        if convert_numerals('Latin', n) == convert_numerals('Latin', '1'):
          if convert_numerals('Latin', m) == convert_numerals('Latin', '2'):
            print(f'great!')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_ifs_nested_in_if_else(self):
        code = textwrap.dedent("""\
        n is 1
        m is 2
        if n is 1
            if m is 2
                print 'great!'
        else
            if m is 3
                print 'awesome'""")

        expected = textwrap.dedent("""\
        n = '1'
        m = '2'
        if convert_numerals('Latin', n) == convert_numerals('Latin', '1'):
          if convert_numerals('Latin', m) == convert_numerals('Latin', '2'):
            print(f'great!')
        else:
          if convert_numerals('Latin', m) == convert_numerals('Latin', '3'):
            print(f'awesome')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_else_nested_in_if(self):
        code = textwrap.dedent("""\
        n is 1
        m is 2
        if n is 1
            if m is 2
                print 'great!'
            else
                print 'awesome'""")

        expected = textwrap.dedent("""\
        n = '1'
        m = '2'
        if convert_numerals('Latin', n) == convert_numerals('Latin', '1'):
          if convert_numerals('Latin', m) == convert_numerals('Latin', '2'):
            print(f'great!')
          else:
            print(f'awesome')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_else_statements_nested_in_if_else(self):
        code = textwrap.dedent("""\
         n is 1
         m is 2
         if n is 1
             if m is 2
                 print 'great!'
             else
                 print 'nice!'
         else
             if m is 3
                 print 'awesome!'
             else
                 print 'amazing!'""")

        expected = textwrap.dedent("""\
         n = '1'
         m = '2'
         if convert_numerals('Latin', n) == convert_numerals('Latin', '1'):
           if convert_numerals('Latin', m) == convert_numerals('Latin', '2'):
             print(f'great!')
           else:
             print(f'nice!')
         else:
           if convert_numerals('Latin', m) == convert_numerals('Latin', '3'):
             print(f'awesome!')
           else:
             print(f'amazing!')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    #
    # repeat nesting
    #
    def test_repeat_nested_in_repeat(self):
        code = textwrap.dedent("""\
        repeat 2 times
            repeat 3 times
                print 'hello'""")

        expected = textwrap.dedent("""\
           for i in range(int('2')):
             for i in range(int('3')):
               print(f'hello')
               time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    #
    # if and repeat nesting
    #
    def test_if_nested_in_repeat(self):
        code = textwrap.dedent("""\
        prijs is 0
        repeat 7 times
            ingredient is ask 'wat wil je kopen?'
            if ingredient is appel
                prijs is prijs + 1
        print 'Dat is in totaal ' prijs ' euro.'""")

        expected = textwrap.dedent("""\
        prijs = '0'
        for i in range(int('7')):
          ingredient = input(f'wat wil je kopen?')
          if convert_numerals('Latin', ingredient) == convert_numerals('Latin', 'appel'):
            prijs = int(prijs) + int(1)
          time.sleep(0.1)
        print(f'Dat is in totaal {prijs} euro.')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_if_nested_in_repeat_with_comment(self):
        code = textwrap.dedent("""\
        prijs is 0
        repeat 7 times # comment
            ingredient is ask 'wat wil je kopen?'
            if ingredient is appel # another comment
                prijs is prijs + 1
        print 'Dat is in totaal ' prijs ' euro.'""")

        expected = textwrap.dedent("""\
        prijs = '0'
        for i in range(int('7')):
          ingredient = input(f'wat wil je kopen?')
          if convert_numerals('Latin', ingredient) == convert_numerals('Latin', 'appel'):
            prijs = int(prijs) + int(1)
          time.sleep(0.1)
        print(f'Dat is in totaal {prijs} euro.')""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_repeat_nested_in_if(self):
        code = textwrap.dedent("""\
        kleur is groen
        if kleur is groen
            repeat 3 times
                print 'mooi'""")

        expected = textwrap.dedent("""\
        kleur = 'groen'
        if convert_numerals('Latin', kleur) == convert_numerals('Latin', 'groen'):
          for i in range(int('3')):
            print(f'mooi')
            time.sleep(0.1)""")

        self.multi_level_tester(
            code=code,
            expected=expected,
            max_level=11,
            expected_commands=['is', 'if', 'repeat', 'print'])

    def test_if_else_nested_in_repeat(self):
        code = textwrap.dedent("""\
        repeat 5 times
            if antwoord2 is 10
                print 'Goedzo'
            else
                print 'lalala'""")

        expected = textwrap.dedent("""\
        for i in range(int('5')):
          if convert_numerals('Latin', 'antwoord2') == convert_numerals('Latin', '10'):
            print(f'Goedzo')
          else:
            print(f'lalala')
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    #
    # if pressed repeat tests
    #

    def test_if_pressed_repeat(self):
        code = textwrap.dedent("""\
        if x is pressed
            repeat 5 times
                print 'doe het 5 keer!'
        else
            print '1 keertje'""")

        expected = HedyTester.dedent("""\
        pygame_end = False
        while not pygame_end:
          pygame.display.update()
          event = pygame.event.wait()
          if event.type == pygame.QUIT:
            pygame_end = True
            pygame.quit()
            break
          if event.type == pygame.KEYDOWN:
            if event.unicode == 'x':
              for i in range(int('5')):
                print(f'doe het 5 keer!')
                time.sleep(0.1)
              break
            # End of PyGame Event Handler    
            else:
              print(f'1 keertje')
              break""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    #
    # button tests
    #

    def test_if_button_is_pressed_print_in_repeat(self):
        code = textwrap.dedent("""\
        button1 is button
        repeat 3 times
          if button1 is pressed
            print 'wow'
          else
            print 'nah'""")

        expected = HedyTester.dedent(f"""\
        create_button('button1')
        for i in range(int('3')):
          pygame_end = False
          while not pygame_end:
            pygame.display.update()
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
              pygame_end = True
              pygame.quit()
              break
            if event.type == pygame.USEREVENT:
              if event.key == 'button1':
                print(f'wow')
                break
              # End of PyGame Event Handler    
              else:
                print(f'nah')
                break
          time.sleep(0.1)""")

        self.multi_level_tester(code=code, expected=expected, max_level=11)

    def test_source_map(self):
        code = textwrap.dedent("""\
        repeat 3 times
            food = ask 'What do you want?'
            if food is pizza
                print 'nice!'
            else
                print 'pizza is better'""")

        expected_source_map = {
            "1/0-6/160": "1/0-7/214",
            "1/0-6/161": "1/0-7/214",
            "2/19-2/23": "2/28-2/32",
            "2/19-2/49": "2/28-2/62",
            "3/57-3/70": "3/68-3/137",
            "3/54-4/101": "7/-1-7/90",
            "3/54-6/151": "7/-1-7/124",
            "4/79-4/92": "4/143-4/158",
            "4/101-6/151": "7/-1-7/33",
            "6/119-6/142": "6/171-6/196"
        }

        self.source_map_tester(
            code=code,
            expected_source_map=expected_source_map,
        )

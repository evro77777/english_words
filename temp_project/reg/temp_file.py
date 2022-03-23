def addquery(request):
    if request.method == 'POST':
        obj = copy.deepcopy(request.POST)
        obj['answer_options'] = ['1','2','3','4']
        obj['english_word'] = 'some_word'
        obj['right_answer'] = 'right_answer'
        form = HomeForm(obj)
        english_word = form.english_word

        if form.is_valid():
            form = HomeForm(word_and_answer_options())
            answer = form.cleaned_data['choice_field']
            right_answer = form.right_answer
            if answer == right_answer:
                form = HomeForm(word_and_answer_options())
                print('form=',form)
                english_word = form.english_word
                return render(request, 'reg/home.html', {'form': form, 'english_word': english_word})
        else:
            print('inside else')
    else:
        def addquery(request):
            if request.method == 'POST':
                obj = copy.deepcopy(request.POST)
                obj['answer_options'] = ['1', '2', '3', '4']
                obj['english_word'] = 'some_word'
                obj['right_answer'] = 'right_answer'
                form = HomeForm(obj)
                english_word = form.english_word

                if form.is_valid():
                    form = HomeForm(word_and_answer_options())
                    answer = form.cleaned_data['choice_field']
                    right_answer = form.right_answer
                    if answer == right_answer:
                        form = HomeForm(word_and_answer_options())
                        print('form=', form)
                        english_word = form.english_word
                        return render(request, 'reg/home.html', {'form': form, 'english_word': english_word})
                else:
                    print('inside else')
            else:
                form = HomeForm(word_and_answer_options())
                english_word = form.english_word
                print('form.egglish_word=', form.choice_field)
            return render(request, 'reg/home.html', {'form': form, 'english_word': english_word})
        print('form.egglish_word=',form.choice_field)
    return render(request, 'reg/home.html', {'form': form, 'english_word':english_word})
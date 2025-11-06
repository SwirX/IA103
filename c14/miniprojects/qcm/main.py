import json
from math import floor


class QCM():
    def __init__(self):
        self.questions_file = 'questions.json'
        self.charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # values
        self.debug_state = True
        self.questions = []
        self.score = 0
        self.idx = 0
        self.running = False

        self.main()

    def main(self):
        c = int(input('1 -> start\n2 -> add questions\n> '))
        if c == 1:
            self.load()
            self.run()
        elif c == 2:
            self.add_questions()
        else:
            print('stupid')
            exit(1)

    def _num_2_alpha(self, num:int) -> str:
        return self.charset[num]
        #mod = num%len(self.charset)
        #print(f'mod: {mod}')
        #if mod != 0:
        #    ret = (len(self.charset) * mod) - num
        #    return self.charset[mod] + self.charset[ret]
        #else:
        #    return self.charset[num]

    def _alpha_2_num(self, alpha:str) -> int:
        self.debug(f'converting {alpha} to number')
        alpha = alpha.upper()
        if len(alpha) == 1:
            return self.charset.find(alpha)
    
    def _load_questions(self) -> None:
        self.debug('loading questions from file')
        with open(self.questions_file) as f:
            self.questions = json.load(f)

    def _load_scores(self):
        pass 

    def load(self):
        self._load_questions()
        self._load_scores()

    def _save_score(self):
        pass

    def _save_questions(self):
        self.debug('saving the file')
        with open(self.questions_file, 'w+') as f:
            json.dump(self.questions, f, indent=4)
        return

    def save(self):
        self._save_questions()
        self._save_score()

    def _populate(self):
        question_str = input('Question > ')
        count = int(input('Answers Count > '))
        choices = []
        for i in range(count):
            choice = input('Enter choice > ')
            choices.append(choice)
        idx = int(input('index of correct question > '))
        question = {
                'question': question_str,
                'choices': choices,
                'answer': idx
                }
        self.questions.append(question)

    def add_questions(self):
        while True:
            self._populate()
            if input('q -> quit, Enter -> continue\n> ') in ['q', 'quit', 'exit']:
                break
        self.save()

    def debug(self, *args):
        if self.debug_state == False:
            return
        for i in args:
            print(i)

    def run(self):
        self.running = True
        while self.running and self.idx+1 == len(self.questions):
            self.debug(f'index = {self.idx}')
            q = self.questions[self.idx]
            print(q['question'])
            for i, c in enumerate(q['choices']):
                alpha = self._num_2_alpha(i)
                print(f'{alpha}) {c}')
            choice = input('Select one of the choices > ')
            num_choice = self._alpha_2_num(choice)
            if num_choice < len(q['choices']):
                if num_choice == q['answer']:
                    print('Correct!')
                    self.score += 1
                else:
                    print('Incorrect!')
                    correct_idx = q['answer']
                    correct_str = self._num_2_alpha(correct_idx)
                    print(f'la reponse correcte est: \n{correct_str}) {q['choices'][correct_idx]}')

            self.idx += 1

        print(f'{self.score}/{len(self.questions)}')


if __name__ == '__main__':
    QCM()

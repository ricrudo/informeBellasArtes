from pathlib import Path
import re
path_ = Path.cwd() / 'app' / 'domain' / 'models.py'

text = path_.read_text()

a = re.findall(r'class (.*)\(', text)

content = ''

for ele in a:
    content += f'''
    def test_{ele}(self):
        p = self.session.query(models.Person).filter_by(last_names="Ost Bers").first()
        valid_data = models.{ele}(
            id_person = p.id
        )
        #self.session.add(valid_data)
        #self.session.commit()
        #r = self.session.query(models.{ele}).filter_by(id_person=p.id).first()
    '''

path_2 = Path.cwd() / 'test' / 'domain' / 'copy.txt'

path_2.write_text(content)

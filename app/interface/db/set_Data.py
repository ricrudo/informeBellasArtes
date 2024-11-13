from app.interface.db import db_manager

from app.interface import db

from app.interface.db import section1_1
from app.interface.db import section2_1
from app.interface.db import section2_2
from app.interface.db import section3_1
from app.interface.db import section4_1
from app.interface.db import section4_2
from app.interface.db import section4_3
from app.interface.db import section4_4
from app.interface.db import section4_5
from app.interface.db import section4_6
from app.interface.db import section4_7
from app.interface.db import section4_8
from app.interface.db import section4_9
from app.interface.db import section4_10
from app.interface.db import section4_11
from app.interface.db import section4_12
from app.interface.db import section4_13
from app.interface.db import section4_14
from app.interface.db import section4_15
from app.interface.db import section4_16
from app.interface.db import section4_17
from app.interface.db import section5_1
from app.interface.db import section5_2
from app.interface.db import section5_3
from app.interface.db import section6_1
from app.interface.db import section6_2
from app.interface.db import section6_3
from app.interface.db import section6_4
from app.interface.db import section6_5
from app.interface.db import section6_6
from app.interface.db import section6_7

from app.domain.models import ActiveSections

def getSection(section):
    sections = {
        'section1_1': section1_1,
        'section2_1': section2_1,
        'section2_2': section2_2,
        'section3_1': section3_1,
        'section4_1': section4_1,
        'section4_2': section4_2,
        'section4_3': section4_3,
        'section4_4': section4_4,
        'section4_5': section4_5,
        'section4_6': section4_6,
        'section4_7': section4_7,
        'section4_8': section4_8,
        'section4_9': section4_9,
        'section4_10': section4_10,
        'section4_11': section4_11,
        'section4_12': section4_12,
        'section4_13': section4_13,
        'section4_14': section4_14,
        'section4_15': section4_15,
        'section4_16': section4_16,
        'section4_17': section4_17,
        'section5_1': section5_1,
        'section5_2': section5_2,
        'section5_3': section5_3,
        'section6_1': section6_1,
        'section6_2': section6_2,
        'section6_3': section6_3,
        'section6_4': section6_4,
        'section6_5': section6_5,
        'section6_6': section6_6,
        'section6_7': section6_7
    }
    return sections.get(section, 'question no valida')


def setData(jsonData):
    messages = []
    for store in jsonData.keys():
        if store.startswith('section'):
            section = getSection(store)
            saveData = True
            deleteData = False
            activeQuestion = jsonData[store].get(f'activateQuestion{store}', 'No_contiene')
            if activeQuestion in ('No_contiene', 'si'):
                pass
            elif activeQuestion in ['no', '']:
                saveData = False
                deleteData = True
            if saveData:
                if section == 'question no valida':
                    messages.append(section)
                    return messages
                response = section.new_entry_user(jsonData)
                if response != 'ok':
                    messages.append(response)
            if activeQuestion in ['si', 'no', '']:
                content = {
                    f'activateQuestion{store}': activeQuestion,
                    'user': jsonData['user'],
                    'period_spam': jsonData['period_spam']
                } 
                entry = db_manager._check_entry(content, ActiveSections, index_entry=False)
                if entry:
                    db_manager._update_entry(entry, content)
                else:
                    create_entry_activeQuestion(content)

def create_entry_activeQuestion(content):
    entry = ActiveSections(
        id_person = content['user'],
        activateQuestionsection4_1  = content.get('activateQuestionsection4_1',  ''),  
        activateQuestionsection4_3  = content.get('activateQuestionsection4_3',  ''),
        activateQuestionsection4_4  = content.get('activateQuestionsection4_4',  ''),
        activateQuestionsection4_5  = content.get('activateQuestionsection4_5',  ''),
        activateQuestionsection4_6  = content.get('activateQuestionsection4_6',  ''),
        activateQuestionsection4_7  = content.get('activateQuestionsection4_7',  ''),
        activateQuestionsection4_8  = content.get('activateQuestionsection4_8',  ''),
        activateQuestionsection4_9  = content.get('activateQuestionsection4_9',  ''),
        activateQuestionsection4_10 = content.get('activateQuestionsection4_10', ''),
        activateQuestionsection4_11 = content.get('activateQuestionsection4_11', ''),
        activateQuestionsection4_12 = content.get('activateQuestionsection4_12', ''),
        activateQuestionsection4_13 = content.get('activateQuestionsection4_13', ''),
        activateQuestionsection4_14 = content.get('activateQuestionsection4_14', ''),
        activateQuestionsection4_15 = content.get('activateQuestionsection4_15', ''),
        activateQuestionsection4_16 = content.get('activateQuestionsection4_16', ''),
        activateQuestionsection4_17 = content.get('activateQuestionsection4_17', ''),
        activateQuestionsection5_1  = content.get('activateQuestionsection5_1',  ''),
        activateQuestionsection5_2  = content.get('activateQuestionsection5_2',  ''),
        activateQuestionsection5_3  = content.get('activateQuestionsection5_3',  ''),
        activateQuestionsection6_2  = content.get('activateQuestionsection6_2',  ''),
        activateQuestionsection6_3  = content.get('activateQuestionsection6_3',  ''),
        activateQuestionsection6_4  = content.get('activateQuestionsection6_4',  ''),
        activateQuestionsection6_5  = content.get('activateQuestionsection6_5',  ''),
        activateQuestionsection6_6  = content.get('activateQuestionsection6_6',  ''),
        activateQuestionsection6_7  = content.get('activateQuestionsection6_7',  ''),
        period_spam = content['period_spam']
    )
    db.session.add(entry)
    db.session.commit()
    
                


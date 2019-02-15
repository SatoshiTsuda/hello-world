#! python3
# JPhoneAndEmail.py - �N���b�v�{�[�h����d�b�ԍ��ƃ��A�h����������i���{��Łj

import pyperclip, re

#phone_regex = re.compile(r'''(
#    (\d{3}|\(\d{3}\))?               # �s�O�ǔ�
#    (\s|-|\.)?                       # ��؂�
#    (\d{3})                          # 3���̔ԍ�
#    (\s|-|\.)                        # ��؂�
#    (\d{4})                          # 4���̔ԍ�
#    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # �����ԍ�
#    )''', re.VERBOSE)

# ���{�̓d�b�ԍ��p�^�[���ɂ�������
phone_regex = re.compile(r'''(
    (0\d{0,3}|\(\d{0,3}\))           # �s�O�ǔ�
    (\s|-)                           # ��؂�
    (\d{1,4})                        # �s���ǔ�
    (\s|-)                           # ��؂�
    (\d{3,4})                        # �����Ҕԍ�
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # �����ԍ�
    )''', re.VERBOSE)


# �d�q���[���̐��K�\�������B
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # ���[�U�[��
    @                  # @ �L��
    [a-zA-Z0-9.-]+     # �h���C����
    (\.[a-zA-Z]{2,4})  # �h�b�g�Ȃ�Ƃ�
    )''', re.VERBOSE)

# �N���b�v�{�[�h�̃e�L�X�g����������B
text = str(pyperclip.paste())
matches = []  #
for groups in phone_regex.findall(text):  #
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):  #
    matches.append(groups[0])

# �������ʂ��N���b�v�{�[�h�ɓ\��t����B
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('�N���b�v�{�[�h�ɃR�s�[���܂���:')
    print('\n'.join(matches))
else:
print('�d�b�ԍ��⃁�[���A�h���X�͌�����܂���ł����B')
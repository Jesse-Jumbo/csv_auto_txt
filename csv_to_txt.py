from field_name import *
import pandas as pd

encoding_list = ['ascii', 'big5', 'big5hkscs', 'cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720', 'cp737'
                 , 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862'
                 , 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950'
                 , 'cp1006', 'cp1026', 'cp1125', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254'
                 , 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr'
                 , 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2'
                 , 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'latin_1', 'iso8859_2'
                 , 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9'
                 , 'iso8859_10', 'iso8859_11', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab'
                 , 'koi8_r', 'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2'
                 , 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32'
                 , 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig']

if DEBUG:
    for encoding in encoding_list:
        worked = True
        try:
            df = pd.read_csv(IMPORT_FILE, encoding=encoding, nrows=5)
        except:
            worked = False
        if worked:
            print(encoding, ':\n', df.head())
try:
    df = pd.read_csv(IMPORT_FILE, encoding=READ_ENCODING)

    for key in df.keys():
        for file_name in df[key]:
            if file_name == DONOR:
                donor = df[key]
            if file_name == DONATION_AMOUNT:
                donation_amount = df[key]
            if file_name == IMPORT_DATE:
                import_date = df[key]
            if file_name == RECEIPT:
                receipt = df[key]
            if file_name == TAXI:
                taxi = df[key]
            if file_name == EMAIL:
                email = df[key]
            if file_name == SOURCE:
                source = df[key]


    def get_field_name(field_name):
        for key in df.keys():
            if file_name == field_name:
                return key
except BaseException as e:
    print("Error: ", e)
else:
    print("Please input the line number: ", end="")
    index = int(input())
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-16") as w_f:
            # w_f.write("\ufeff")
            w_f.write(f"{email[index]}\n")
            w_f.write("[PTWA]????????????\n")
            w_f.write("?????????" + donor[index] + "??????\n")
            w_f.write("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????PTWA ????????????????????????????????????\n")
            w_f.write(f"?????????      {donor[index]}\n")
            if "??????" in source[index]:
                w_f.write(f"????????????   {donation_amount[index]}???/???\n")
            else:
                w_f.write(f"????????????   {donation_amount[index]}???\n")
            w_f.write(f"????????????    {import_date[index]}\n")
            if receipt[index] == "N" and taxi[index] == "N":
                w_f.write("????????????    (?????????????????? ??????????????????)\n")
            else:
                if receipt[index] == "Y":
                    w_f.write("????????????    ????????????\n")
                elif receipt[index] == "M":
                    w_f.write("????????????    ???????????????\n")
                elif receipt[index] == "N":
                    w_f.write("????????????    ??????\n")
                else:
                    w_f.write("????????????    \n")
                if taxi[index] == "Y":
                    w_f.write("           ??????????????????????????????\n")
                else:
                    w_f.write("           ???????????????\n")
            w_f.write("\n????????????????????????????????????????????????\n")
            w_f.write("???????????????https://programtheworld.tw/main.php\n")
            w_f.write("FB ???????????? https://www.facebook.com/program.the.world/\n")
            w_f.write("????????????YouTube???????????? ???????????????????????????????????????????????????\n")
            w_f.write("\n")
            w_f.write("??????????????????????????????????????? ???????????? ????????????")
    except BaseException as e:
        print("Error: ", e)

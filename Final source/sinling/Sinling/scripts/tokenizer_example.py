from sinling.sinhala.tokenizer import SinhalaTweetTokenizer

if __name__ == '__main__':
    docs = [
        'මමත් රජයේ විශ්ව විද්‍යාලයකට තමා ගියේ, හැබැයි මම නම් හැමදාම කැම්පස් එකේ CCTV සවි කරන එක හොඳයි'
        ' කියන අදහසේ හිටියා අදත් එහෙමයි. රැග් එක නවත්තන්න එ්ක හොඳ උදව්වක්. අැයි පේරාදෙණියේ කට්ටිය එ්වට'
        ' එච්චර බය...? 😂😂😂 #lka #Srilanka',
        'ගොඩක් අයට ඩෙංගු හැදිල. මම බය වෙන්නෙ හැදුණොත් අනිත් අයට කරදර කරන්න වෙන නිසා. 😱 😱 #ඩෙංගු',
        'හෙට පේපර් එකට කුණුහරුප ලියවෙයි ද කියලයි බය.',
        'අම්මෝ ඒකට යන්න බය හිතුනා ප්‍රොපයිල් එක දැකලා😂😂',
        'බය වෙන්න එපො, ඔය තරම්',
        'Self love එක වැඩි උනාම selfish වෙනෝ ලු. ඒක නිසා බය හිතෙනෝ. 😅😄🙏👍',
        '@RW_UNP චිවරදාරින්ට ඔනෑම අපරාධයක් කිරිමට ලයිසන් දෙනවා විතරක් නෙමෙයි එයාලව ආරක්ශා කරන්න ප්‍රසිද්ධියේ'
        ' පෙනිහිටිම ඉතාම භයානකයි.. කහ සිවුරට මේච්චර බය ඇයි? එතකොට මේ අපරාධ කරන අයව කරුනු දක්වන්න'
        ' වඩම්මන්නේ නැද්ද?  @RamanayakeR https://pbs.twimg.com/media/D_vLaovUcAAGjQ_.jpg',
        'ආපදා මරණ 4ක් - කළු ගඟේ අවදානම තවදුරටත් - අදත් ප්‍රදේශ රැසකට තද වැසි සමඟ සුළං\n'
        'watch more>>>\n'
        'https://bit.ly/2XQbNYH',
        'හිසුබ්ල්ලාගේ ෂරියා විශ්ව විද්‍යාලයට සෞදි තහනම් සංවිධානයකින් කොටි 1757ක්\n'
        'Read more>>>\n'
        'https://bit.ly/2xXSRYx'
    ]
    tokenizer = SinhalaTweetTokenizer()
    # tokenizer = SinhalaTokenizer()
    for doc in docs:
        for sent in tokenizer.split_sentences(doc):
            print(tokenizer.tokenize(sent))

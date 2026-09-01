# -*- coding: utf-8 -*-
"""
Script dịch và chuẩn hóa 18 file hmr novel của commit 4f109c0c
- hmr_10220100011 -> hmr_10220100033 (Yuri)
- hmr_11030100011 -> hmr_11030100033 (Naia)
Tuân thủ nghiêm ngặt TRANSLATION_GUIDE_SUMMARY.md:
1. Tối đa 1 thẻ <br> (tối đa 2 dòng/hộp thoại).
2. Chiều dài mỗi dòng lên đến 70 ký tự.
3. Không có <br> ở đầu hoặc cuối câu.
4. Xưng hô: Tư lệnh / anh Tư lệnh, Chủ nhân, em - anh, Yuri, Naia, v.v.
5. Thuật ngữ H-scene: dương vật, thanh thịt, dâm dịch, tinh dịch, nơi thầm kín, môi dưới, lỗ sáo, tự sướng, v.v.
6. Nữ lên đỉnh: ra, ra đây, lên đỉnh (Không dùng bắn tinh cho nữ).
7. Nam xuất tinh: bắn vào trong, phóng thích tinh dịch.
"""
import json
import os
import re
from pathlib import Path

ROOT_DIR = Path(r"d:\idontknow\dotabyss-translation")
NOVELS_DIR = ROOT_DIR / "translations" / "novels"

DATA = {}

# ==========================================
# 1. YURI (hmr_1022)
# ==========================================

DATA["hmr_10220100011"] = {
    "激しい雨音が洞窟の外で轟いている。<br>一歩先も見えない濃霧と、体温を夺い去る冷たい雨。": "Tiếng mưa dữ dội ầm ầm ngoài hang động.<br>Màn sương mù dày đặc che khuất tầm nhìn và cơn mưa buốt giá.",
    "暗い洞窟の奥で、<user>とユーリの<br>ふたりの荒い吐息だけが重なり合うように響いていた――": "Sâu trong hang tối, chỉ còn lại tiếng thở dồn dập<br>của <user> và Yuri hòa quyện vào nhau――",
    "はぁ、はぁ……。<br>ここならば、ひとまず……雨風は凌げるはずだ。": "Hà... hà...<br>Ở đây tạm thời có thể tránh được mưa gió rồi.",
    "はぁ、はぁ……。<br>霧で皆さんの姿が見えなくなった時はどうなることかと思いました……": "Hà... hà... Lúc sương mù che khuất mọi người,<br>em cứ tưởng là có chuyện chẳng lành rồi chứ...",
    "ユーリの細い肩が小刻みに震えている。薄い生地の服は完全に張り付き、<br>彼女の瑞々しいボディラインを無防備に晒していた。": "Bờ vai mảnh mai của Yuri khẽ run. Lớp áo mỏng ướt sũng dính chặt,<br>để lộ những đường cong thiếu nữ nuột nà đầy gợi cảm.",
    "でも……これは、しばらく降りやみそうにないですね……。<br>天候が落ち着くまでは、この洞窟でじっとしていたほうがよさそうです。": "Nhưng... mưa thế này chắc chưa tạnh ngay đâu ạ...<br>Tốt nhất ta nên ở yên trong hang chờ thời tiết ổn định lại.",
    "確かにな。この大雨と濃霧の中で移動するのは危険だ。<br>いつ止むか分からないが、ここでしばらく休憩だな。": "Đúng vậy. Đi lại trong mưa to và sương mù thế này rất nguy hiểm.<br>Dù chưa biết khi nào tạnh, cứ tạm nghỉ ở đây đã.",
    "……あの、しれー。あ、あの……こんな時に不謹慎かもしれませんが、<br>ずっと、気になっていたことがあって……": "Tư lệnh ơi... Chuyện này lúc này có hơi không phải phép,<br>nhưng có một điều em cứ thắc mắc mãi...",
    "……なんだ？ <br>気を紛らわせるためだ、なんでも話してみろ。": "Chuyện gì thế?<br>Cứ nói đi, coi như để phân tán sự chú ý.",
    "……酒場の、２階のことです。夜、お食事をしていると、いつも、<br>綺麗なドレスを着た女性が、男の人と階段を上がっていきますよね。": "Là chuyện trên tầng hai quán rượu ạ. Mỗi tối lúc ăn cơm,<br>em luôn thấy những cô gái diện váy đẹp cùng đàn ông bước lên lầu.",
    "……あそこで、皆さんは何をされているのでしょうか？": "Ở trên đó... mọi người đang làm gì vậy ạ?",
    "あ～……あれはだな、男と女の大人のコミュニケーションというか……<br>つまり――": "À... đó là chuyện giao lưu của người lớn giữa nam và nữ...<br>Nói tóm lại là――",
    "そ、そんなことをしていたのですか……！<br>……は、初めて知りました！": "H-Hóa ra là làm chuyện đó sao...!?<br>L-Lần đầu tiên em mới biết đấy ạ!",
    "まぁ、そういう大人の世界があるってことだ。": "Thì trên đời luôn có thế giới người lớn như vậy mà.",
    "た、確かに……わたしには未知の世界のお話でした……。<br>そっかぁ～……そんなことをされていたんですね……": "Đ-Đúng là một thế giới hoàn toàn xa lạ với em...<br>Ra là vậy... Hóa ra họ làm chuyện đó ư...",
    "ユーリは、初めて知った『大人の世界』に、<br>赤面しながらも興奮しっぱなしの様子だ。": "Yuri đỏ bừng mặt khi lần đầu biết đến 'thế giới người lớn',<br>nhưng vẻ mặt lại không giấu nổi sự phấn khích tò mò.",
    "あ、あの……！　その娼館っていう場所のこと、<br>もっと詳しく教えてもらえませんか……？": "A-Anh Tư lệnh...! Về nơi gọi là kỹ viện đó,<br>anh có thể kể cho em nghe chi tiết hơn được không...?",
    "ユーリは、娼館に興味津々のようで、<br>食い気味に質問を投げかけてくる。": "Yuri tỏ ra vô cùng hiếu kỳ về kỹ viện,<br>háo hức dồn dập đặt câu hỏi.",
    "あそこは客を満足させるためのプロの世界なんだ。<br>働くには、まずは俺との『研修』が必要でだな……": "Đó là nơi làm việc chuyên nghiệp để phục vụ khách.<br>Muốn làm ở đó thì trước tiên phải 'tập huấn' với anh đã...",
    "しれーと……け、けけっ、研修……っ！？<br>それは、その……あの方たちのようなことを、しれーと……？": "T-Tập huấn với anh Tư lệnh...!?<br>Tức là... làm chuyện giống như những người đó với anh...?",
    "ユーリは、そのまま押し黙ってしまう。<br>激しい雨音と、ユーリの心臓の鼓動が聞こえてきそうなほどの静寂――": "Yuri bỗng im bặt. Giữa tiếng mưa rào xối xả,<br>không gian tĩnh lặng tới mức nghe rõ cả tiếng tim cô đập――",
    "……は、はくしょんっ！<br>くそっ、この寒さは流石に堪えるな……": "Hắt... hắt xì!<br>Chết tiệt, lạnh thế này đúng là chịu không thấu...",
    "気温が下がってきたみたいですね……。<br>急いで火を起こしますね。": "Hình như nhiệt độ đang hạ thấp rồi...<br>Em sẽ đi nhóm lửa ngay.",
    "あと、濡れた服は脱いでしまった方がいいです。<br>このままだと体温を奪われてしまって危険です。": "Với lại, anh nên cởi đồ ướt ra đi ạ.<br>Cứ mặc thế này sẽ bị hạ thân nhiệt, nguy hiểm lắm.",
    "わ、分かった！<br>さすがにユーリは登山の知識が豊富だな。助かるよ。": "A-Anh hiểu rồi! Quả nhiên Yuri am hiểu kiến thức leo núi thật.<br>Cảm ơn em nhiều nhé.",
    "（気温が低すぎる……着替えの服もないですし……。<br>このままじゃ、わたしもしれーも体温がどんどん下がっちゃって危険……）": "(Nhiệt độ thấp quá... lại không có đồ thay...<br>Cứ thế này cả mình lẫn anh Tư lệnh đều bị hạ thân nhiệt mất...)",
    "（こういう時は……。<br>そ、そうだ……！　あの方法しかない……！）": "(Những lúc thế này...<br>Đ-Đúng rồi...! Chỉ còn cách đó thôi...!)",
    "濡れた服を脱いでいると、<br>何やら意を決した表情のユーリが静かにこちらに近づいてくる。": "Trong lúc tôi đang cởi quần áo ướt,<br>Yuri với nét mặt đầy quyết tâm bỗng lặng lẽ tiến lại gần.",
    "あ、あの……このままだとふたりとも体温が低下して危険です。<br>だ、だから、その……し、失礼しますっ！": "A-Anh ơi... Cứ thế này cả hai sẽ bị hạ thân nhiệt mất.<br>V-Vì thế, ừm... x-xin thất lễ ạ!"
}

DATA["hmr_10220100012"] = {
    "ユーリのきめ細やかな肌が吸い付くように密着し、触れ合っている部分から、<br>熱すぎるほどの体温が溶け出して伝わってくる。": "Làn da mịn màng của Yuri áp sát vào người tôi,<br>từng điểm chạm truyền sang hơi ấm nóng hổi.",
    "……驚かせて、すみません。でも、体温を下げずに保つには、<br>こうして人肌同士で温め合うのが、最も効率的なんです……": "...Làm anh giật mình, em xin lỗi. Nhưng để giữ ấm cơ thể,<br>da kề da sưởi ấm cho nhau thế này là hiệu quả nhất...",
    "毅然とした口調を保とうとしているが、こちらに押し当てられた<br>彼女の心臓は、壊れた鐘のように激しく脈打っていた。": "Dù cố giữ giọng điệu bình tĩnh, nhưng trái tim cô đang áp vào ngực tôi<br>lại đập thình thịch như một chiếc chuông vỡ.",
    "ど、どうですか、しれー……？<br>……温かい、ですか……？": "A-Anh thấy thế nào, anh Tư lệnh...?<br>...Có thấy ấm không ạ...?",
    "――ユーリとこうしてると、すごく温かい……<br>そう答える。": "――Ở cạnh Yuri thế này ấm áp lắm...<br>Tôi khẽ đáp.",
    "よかったです……しれーを遭難させた上に風邪までひかせちゃったら、<br>山の案内役として失格ですから。": "Thế thì tốt quá... Để anh gặp nạn lại còn bị cảm lạnh,<br>thì em không xứng làm người dẫn đường leo núi nữa rồi.",
    "義務感を口にする彼女だが、ふと、このあまりにも手慣れた様子が気になり、<br>――こういう救助はよくあるのか？　と問いかけてみる。": "Nghe cô bé nói vì trách nhiệm, tôi tò mò trước cử chỉ thành thục này,<br>――liền hỏi xem cách cứu hộ này có thường xảy ra không.",
    "い、いえ！　知識として知っていただけですっ！　実践は初めてですし、<br>それに……相手が誰でもいいってわけじゃないですよ……": "K-Không đâu ạ! Em chỉ biết trên lý thuyết thôi! Đây là lần đầu thực hành,<br>với lại... đâu phải với ai em cũng làm thế này...",
    "俺が相手ならいいのか……？<br>――そうたずねる。": "Nếu là anh thì được sao...?<br>――Tôi hỏi lại.",
    "……はい。しれーが相手なら……。<br>えっ……あ、あの……": "...Vâng. Nếu là anh Tư lệnh thì...<br>Ủa... ơ, anh ơi...",
    "肯定の返事を聞いた瞬間、<user>の理性は、<br>彼女の濡れた髪から漂う濃密な香りに奪われてしまう。": "Ngay khi nghe câu trả lời đồng ý, lý trí của <user><br>đã bị hương thơm ngạt ngào từ mái tóc ướt của cô cướp mất.",
    "その細い首元に鼻先を埋める。雨に濡れた髪の清涼感。<br>そして、その奥から立ち上る、若々しい女性特有の甘く芳しい体臭――": "Tôi vùi mũi vào chiếc cổ thon thả. Vị thanh mát của tóc ướt,<br>hòa cùng mùi hương cơ thể thiếu nữ ngọt ngào quyến rũ――",
    "し、しれー……どうしたんですか？　そ、そんなにクンクンしないで<br>くださいよぉ……さっき走った時に、汗かいちゃってますからぁ……": "A-Anh Tư lệnh... anh sao thế? Đ-Đừng có hít hà như thế mà...<br>Lúc nãy chạy vội, em đổ mồ hôi rồi đấy ạ...",
    "――汗を掻いてるのはお互い様だ。でも、ユーリのはいい匂いだ……<br>そう耳元で囁く。": "――Cả hai ta đều đổ mồ hôi mà. Nhưng của Yuri thơm lắm...<br>Tôi thì thầm bên tai cô.",
    "そ、そんなこと……な、なんか恥ずかしいですよ……。<br>でも……わたしも、しれーの匂い……好きな匂いです……": "C-Chuyện đó... ngượng chết đi được...<br>Nhưng... em cũng... rất thích mùi hương của anh...",
    "重なり合った体温と、首筋から立ち上る酔いしれるような甘い香りに、<br>抑え込んでいた興奮が、抗いようもなく掻き立てられていく。": "Hơi ấm hòa quyện cùng hương thơm say đắm nơi cần cổ<br>đã thổi bùng dục vọng đang bị kìm nén không thể cưỡng lại.",
    "あっ……んぅ……っ♡": "A... ưm...♡",
    "彼女の白い首筋に、熱い舌を這わせ、<br>湧き上がる欲情を押さえられず、腰を動かし始める。": "Tôi lướt đầu lưỡi nóng rực lên chiếc cổ trắng nõn,<br>không kiềm chế được ham muốn mà bắt đầu đưa đẩy hông.",
    "んっ、ふあぁ……く、くすぐったいです……あっ、はぁぁっ……": "Ưm, a... nh-nhột quá anh ơi... a, hà...",
    "少女特有のきめ細かい肌の質感に興奮が臨界点を超え、<br>熱く屹立した肉棒が、彼女の無防備な陰唇を熱く擦り上げていく。": "Làn da thiếu nữ mịn màng khiến cơn hưng phấn vượt qua giới hạn,<br>thanh thịt cương cứng nóng hổi cọ xát vào môi dưới không phòng bị.",
    "ちょ、ちょっと……ま、待って……！<br>しれーの硬いのが……あ、当たってますぅ～！": "K-Khoan đã... ch-chờ chút...!<br>Cái vật cứng của anh... đ-đang cạ trúng em rồi...!",
    "擦れ合う肉棒と膣口の摩擦が急に緩くなる。<br>ユーリの愛蜜が溢れ出し、それが潤滑油となったのだった。": "Sự ma sát giữa thanh thịt và cửa mình bỗng trở nên trơn tru.<br>Dâm dịch ngọt ngào của Yuri tuôn ra, đóng vai trò như chất bôi trơn.",
    "ま、待って……しれー！　こ、興奮しすぎですよぉ～～～っ！<br>はぁっ、はぁっ……ん、んんっ……！": "K-Khoan đã... anh Tư lệnh! A-Anh hưng phấn quá rồi đóoo!<br>Hà, hà... ưm, ưm...!",
    "潤みきった瞳と、甘い蜜にまみれた感触がさらに興奮を掻き立てる。<br>滑りの良さに任せて、さらに深く、強く腰を叩きつけていく。": "Đôi mắt ngấn lệ cùng mật ngọt ướt đẫm càng kích thích cơn dục vọng.<br>Nhờ sự trơn ướt, tôi thúc hông mạnh mẽ và sâu hơn nữa.",
    "はっ、ぁっ、んぅ～～っ……あっ、ふっ……": "Hà, a, ưm... a, phù...",
    "必死に声を抑えようとして、けれど抑えきれなかった喘ぎ声が洞窟に甘く響く。<br>愛液は肉棒を濡らし、どんどん滑りをよくしていく。": "Tiếng rên rỉ cô bé cố kiềm nén nhưng không thể vang vọng khắp hang.<br>Dâm dịch thấm đẫm thanh thịt, khiến từng cú đẩy càng thêm trơn tru.",
    "と――思っていた以上に滑りがよかったらしく、<br>腰を動かした拍子に肉棒が大きく滑り、亀頭が膣口に当たり――": "Và rồi―― do trơn hơn tưởng tượng, một cú nhấp hông đã làm<br>thanh thịt trượt đi, quy đầu thúc thẳng vào cửa mình――",
    "んっぐ！？　あぁっ！　はぁぁああぁ～～～ッ……！！！": "Ưm...!? Aaa! Haaa...!!!",
    "愛液の潤滑を借りた肉棒は、何の抵抗もなくユーリの狭い入り口を押し開き、<br>そのままの勢いで処女の証を一気に貫いてしまったのだ。": "Nhờ dâm dịch bôi trơn, thanh thịt dễ dàng tách mở lối vào chật hẹp,<br>thừa thắng xông lên xuyên thủng màng trinh của Yuri trong một nhịp.",
    "あっ、ちょ、ちょっと待ってぇ……！<br>これっ、は、入っちゃってますよぅっ！　はうっ……！": "A, kh-khoan đã nào...!<br>Cái này, đ-đút vào trong mất rồi! Hức...!",
    "突き破られた衝撃と、異物に満たされる異様な感覚に、<br>ユーリは目を白黒させて絶句する。": "Cảm giác màng trinh bị xuyên thủng và dị vật lấp đầy bên trong<br>khiến Yuri trợn tròn mắt, kinh ngạc không thốt nên lời.",
    "しかし理性を完全に溶かされた今、<br>湧き上がる欲情を止めることなどできなかった。": "Thế nhưng khi lý trí đã hoàn toàn tan chảy,<br>tôi chẳng thể nào kìm hãm dục vọng đang cuộn trào được nữa.",
    "あっ……！　んっ、はあぁ……っ！": "A...! Ưm, haaa...!",
    "溢れ出す欲情をぶつけるように、下から力強く腰を突き上げ始める。<br>肉と肉が激しく衝突する度に、湿った衝撃音が洞窟の壁に低く反響していく。": "Như muốn trút hết ham muốn, tôi thúc mạnh hông từ bên dưới.<br>Mỗi lần thân xác va chạm dữ dội, tiếng bì bạch vang vọng khắp vách hang.",
    "はぁっ……あぁっ、んっ、やっ……！<br>し、しれー……っ！": "Hà... a, ưm, đừng mà...!<br>A-Anh Tư lệnh...!",
    "一突きごとに最奥を抉られ、ユーリの口からは、<br>もはや言葉にならない、ひきつったような嬌声があふれ出した。": "Mỗi cú thúc đều chạm tới tận cùng, từ miệng Yuri<br>bật ra những tiếng rên kiều mị nghẹn ngào không thành lời.",
    "あ、ぁぐっ……！？<br>ひ、ひゃあぁ……っ、ん、んぅううっ……！！": "A, ưm...!?<br>H-Hyaaa... ưm, ưm...!!",
    "内壁は侵入者を拒むどころか、吸い付くような熱を帯びて肉棒の形状をなぞり、<br>とろけるような粘膜の愛撫を返してくる。": "Thành âm đạo chẳng hề cự tuyệt, mà siết chặt nóng bỏng lấy thanh thịt,<br>như đang dùng lớp niêm mạc mềm mại đáp lại từng nhịp yêu thương.",
    "んっ……んっ……あぁっ……ふあっ……！<br>あぁっ……やっ……！　はっ、あぁん……！": "Ưm... ưm... a... phù...!<br>A... đừng mà...! Hà, a...!",
    "突き上げられるたび、彼女の身体は弓なりに反り、<br>上体を揺らしながら、その激しい衝撃に耐え忍んでいた――": "Mỗi lần bị thúc ngược lên, cơ thể cô bé uốn cong như cánh cung,<br>thân trên rung lắc dữ dội đón nhận từng đợt va chạm――",
    "し……しれー……！<br>こ、これ……き、気持ち……いい……！　あっ……あはぁぁっ！": "A-Anh Tư lệnh...!<br>C-Cái này... s-sướng... quá...! A... aaaa!",
    "いつしかユーリの身体から強張りは消え、快楽の奔流に身を委ね始めていた。<br>そのとき――": "Sự căng thẳng trên người Yuri dần tan biến, cô bắt đầu thả mình<br>vào dòng thác khoái lạc. Đúng lúc đó――",
    "えっ……！？　そ、そんな……な、何これぇ……！<br>勝手に腰、動いちゃう……はンっ……！　あっ、ひゃっ、んぅ……！": "Eh...!? S-Sao lại thế... c-cái gì thế này...!<br>Eo em tự chuyển động mất rồi... a...! A, ưm...!",
    "いつしか、ユーリは自分で腰を振っていた。<br>本能に身を任せ、快感を求めるように自ら腰を艶めかしく動かしている。": "Chẳng biết từ lúc nào, Yuri đã tự lắc lư hông.<br>Thuận theo bản năng, cô bé chủ động đưa đẩy đầy mời gọi để tìm kiếm khoái cảm.",
    "あっ……ぅうんっ……はぁあぁっ！<br>やっ……！　き、気持ち良すぎて……止まんない……！　はぁぁっ！": "A... ưm... haaa!<br>Đừng mà...! S-Sướng quá... không dừng lại được...! Haaa!",
    "自分でも制御できない、本能的な腰の動き。積極的に快楽を貪ろうとする<br>自分の身体に、誰よりもユーリ自身が驚愕していた。": "Chính Yuri là người kinh ngạc nhất trước cơ thể mình,<br>khi chiếc hông cứ tự động đưa đẩy đầy thèm khát khoái lạc.",
    "（やだ……！　しれーの前で、こんなに腰振って……恥ずかしいよぅ……！<br>わたし、こんなにエッチな子だったの……！？）": "(Trời ơi...! Trước mặt anh ấy mà mình lắc hông thế này... xấu hổ quá...!\nHóa ra mình lại là đứa con gái dâm đãng thế này sao...!?)",
    "ご、ごめんなさい……！<br>わたしばっかり、勝手に動いちゃって……あっ、はぁっ……！": "E-Em xin lỗi...!<br>Cứ tự ý chuyển động một mình thế này... a, hà...!",
    "不安そうなユーリに、すごく気持ちいいから大丈夫だと答える。<br>実際、締まったり緩めたりと、緩急のある刺激が何とも言えず気持ちいい。": "Thấy Yuri lo lắng, tôi bảo rằng em làm thế anh sướng lắm.<br>Thực sự những nhịp siết nhả nhịp nhàng bên trong cô bé sướng không tả xiết.",
    "ほんとうですか……？　よかった……。<br>しれー……あの、わたし……このまましれーと気持ち良くなりたいです……": "Thật ạ...? May quá...<br>Anh Tư lệnh ơi... em... muốn cùng anh sướng như thế này tiếp...",
    "だから……最後まで、お願いします。": "Vì thế... xin anh hãy làm tới cùng nhé.",
    "誘うように潤んだ瞳で見つめられ、<br>肉棒がさらに一段階、太く滾っていく。": "Trước ánh mắt đẫm lệ đầy mời gọi ấy,<br>thanh thịt của tôi lại trướng to và nóng rực thêm một bậc.",
    "ひゃぅ……っ！　ああっ、はあぁっ、ぁああ～～～っ……！": "Hyaaa...! Aaa, haaa...!",
    "激しく腰を突き上げるたび、ぎちぎちに張り詰めた肉棒が、<br>ユーリの最奥――子宮の入り口を幾度も力強く叩き上げていく。": "Mỗi cú thúc hông dữ dội, thanh thịt căng cứng như sắt thép<br>lại liên hồi nện thẳng vào nơi sâu nhất―― miệng tử cung của Yuri.",
    "わっ、あぁあっ、はぅっっ……！　こ、これ、すごいっ、すごいですぅ～……！<br>わ、わたしも動きます、ね……しれーを、気持ち良くして、あげなきゃ……！": "Oa, aaa, hức...! C-Cái này tuyệt quá đi mất...!\nE-Em cũng sẽ chuyển động... phải làm cho anh sướng nữa chứ...!",
    "一突きごとに脳髄を焼くような衝撃が走り、<br>ユーリの視界は快楽の火花で白く塗り潰されていく。": "Mỗi nhịp đâm là một luồng điện xé toạc tâm trí,<br>tầm nhìn của Yuri bị pháo hoa của sự sung sướng nhuộm trắng xóa.",
    "あっ、ひっ、はっっ、ひゃうっ……！　あっ、あぁっ、あぁ～～～……っ！<br>も、もう、だめぇ……頭、ボーっとしてきて、くらくらしちゃいますぅ～……！": "A, hức, hà, a...! A, a, aaa...!\nK-Không được rồi... đầu óc em quay cuồng trống rỗng hết cả rồi...!",
    "ユーリの膣壁がビクビクと蠕動し始める。絶頂が近いようだ。<br>とはいえ、限界が近いのはこちらも同じだった。": "Thành âm đạo của Yuri bắt đầu co giật kịch liệt. Có vẻ cô sắp lên đỉnh.<br>Tuy nhiên, tôi cũng đã sắp chạm đến giới hạn.",
    "しれぇ……あっ、やっ……も、もう、わたし……！<br>ひあっ、はっ、あっ、あっっ……！": "Anh Tư lệnh ơi... a, đừng mà... em sắp...!\nA, hà, a, a...!",
    "あっ、あっ、だ、だめぇっ！　ぁああぁぁ～～ッ！！！": "A, a, k-không được rồi! Aaaaa...!!!",
    "絶頂の瞬間、ユーリの身体はビクンビクンと激しく痙攣し、<br>その震える最奥へと熱く濃密な精液が大量に注ぎ込まれていく。": "Khoảnh khắc lên đỉnh, thân thể Yuri giật bắn co thắt dữ dội,<br>dòng tinh dịch nóng hổi đặc quánh bắn xối xả vào nơi sâu nhất.",
    "はぁ、はぁ……はぁ……": "Hà... hà... hà...",
    "静まり返った洞窟に、ふたりの荒い呼吸だけが重なり合う。<br>絶頂の余韻に浸りながら、息を整え、徐々に冷静さを取り戻していくユーリ。": "Trong hang động yên ắng, chỉ còn tiếng thở dốc của hai người.<br>Chìm trong dư âm cực khoái, Yuri dần lấy lại hơi thở và sự bình tĩnh.",
    "（わ、わたし……エッチ、しちゃったんだ……しれーと……！）": "(M-Mình... đã làm chuyện ấy rồi... với anh Tư lệnh...!)",
    "冷静になるにつれ、羞恥心がじわじわと込み上げてくる。<br>ユーリは不安げな瞳でこちらを見つめると、震える声で問いかけた。": "Khi bình tâm lại, cảm giác xấu hổ trào dâng.<br>Yuri nhìn tôi với ánh mắt bồn chồn rồi run run cất tiếng hỏi.",
    "し、しれー……わ、わたし、自分であんなに腰振っちゃって……、<br>変な女の子だと……エ、エッチな女の子だと思っちゃいましたよね……？": "A-Anh ơi... em tự lắc hông nhiều như thế...<br>Anh có thấy em là đứa con gái kỳ lạ... d-dâm đãng không ạ...?",
    "不安そうに一気に言うユーリに、思わず笑みがこぼれる。<br>そんなことないぞ。むしろ、こっちも夢中になってしまったしな――と答える。": "Thấy Yuri lo lắng nói một tràng, tôi bật cười trấn an.<br>Làm gì có chuyện đó, chính anh cũng mê mẩn em đấy thôi―― tôi đáp.",
    "それって、あ、あの……。<br>わたしとエッチなことして、よかったってことですか……？": "Thế tức là, ừm...<br>Làm chuyện ấy với em... anh thấy thích lắm đúng không ạ...?",
    "もちろんだ――と力強く頷いて答えてやる。": "Tất nhiên rồi―― tôi gật đầu quả quyết.",
    "その言葉を聞いたユーリは、張り詰めていた表情をふっと和らげると、<br>どこか安堵したような、慈愛に満ちた柔らかな微笑みを浮かべる。": "Nghe thế, nét mặt căng thẳng của Yuri dịu lại,<br>nở nụ cười hiền từ, ngập tràn sự an tâm và yêu thương.",
    "……。<br>……よかった……": "...<br>...May quá rồi..."
}

DATA["hmr_10220100013"] = {
    "洞窟の外を支配していた猛烈な雨音は、いつの間にか止んでいた。<br>岩の隙間から差し込む太陽の光が、湿った地面をキラキラと照らしている。": "Tiếng mưa rào dữ dội ngoài hang đã tạnh từ lúc nào.<br>Tia nắng rọi qua kẽ đá, chiếu sáng nền đất ẩm ướt lấp lánh.",
    "すっかり天気もよくなりましたね。": "Thời tiết đã đẹp trở lại rồi ạ.",
    "ああ。だが、早いところ帰還しないとな。<br>遭難したと思われて、捜索隊が出ているかもしれない。": "Ừ. Nhưng ta phải mau chóng trở về thôi.<br>Mọi người tưởng ta gặp nạn có khi đang cử đội tìm kiếm rồi.",
    "あ、あの……本当に、わたしのこと、<br>エッチな女の子だと思ってません……よね？": "A-Anh ơi... anh thực sự không nghĩ em<br>là đứa con gái dâm đãng đấy chứ...?",
    "ユーリは、昨夜の自分が見せた積極的な振る舞いを思い出し、<br>顔を赤らめて俯いてしまう。": "Yuri nhớ lại những hành động chủ động tối qua,<br>mặt đỏ bừng bối rối cúi gằm xuống.",
    "ふ、普段からエッチなわけじゃないんですよ？　そ、その……神殿で育った<br>ものですから、そこでの戒律が結構厳しくて、そ、その反動というか……": "B-Bình thường em không thế đâu ạ! T-Tại vì em lớn lên ở thần điện,<br>giới luật khắt khe quá nên... có lẽ là bị dồn nén...",
    "別に気にすることはない。<br>昨晩のユーリ、すごく魅力的だったぞ。": "Không cần bận tâm đâu.<br>Tối qua trông Yuri quyến rũ lắm.",
    "う、うぅぅ～～……またそんな恥ずかしいことを～……": "Ư... anh lại trêu làm em ngượng nữa rồi...",
    "それで……一応、流れとはいえ、<br>俺との研修はこれで終わったことにもなるんだが……。": "Thế... coi như theo dòng sự việc,<br>buổi tập huấn với anh cũng xem như kết thúc rồi...",
    "どうだ？　まだ娼館に興味はあるのか？": "Sao nào? Em còn hứng thú với kỹ viện nữa không?",
    "……そう、ですね。興味があるのは確かですけど、<br>今はどちらかというと、その……": "...Dạ có. Hứng thú thì vẫn có,<br>nhưng bây giờ thì, ừm...",
    "……？": "...?",
    "し、しれーとのエッチがもっとうまくできるようになったらいいな、って……。<br>そう、思ってます……": "Em muốn... làm chuyện ấy với anh Tư lệnh giỏi hơn nữa...<br>Em đang nghĩ thế ạ...",
    "恥ずかしそうに、けれど真っ直ぐに想いを口にするユーリ。<br>その時、遠くの丘に人影が見えた。前線基地の捜索隊と思われる一団だ。": "Yuri bẽn lẽn nhưng thẳng thắn bộc bạch tâm tư.<br>Đúng lúc ấy, đằng xa xuất hiện bóng người của đội tìm kiếm.",
    "あ、あれは……捜索隊か。<br>どうやら見つかったみたいだな。ユーリ、無事に帰れるぞ。": "A, đằng kia... đội cứu hộ kìa.<br>Tìm thấy chúng ta rồi. Yuri, mình có thể an toàn về rồi.",
    "そ、そうですね……！": "V-Vâng ạ...!",
    "……しれーをもっと気持ち良くさせるには、<br>やっぱり娼館で腕を磨く方がいいのかな……": "(...Để làm anh Tư lệnh sướng hơn nữa,<br>có khi đến kỹ viện rèn luyện tay nghề sẽ tốt hơn chăng...)",
    "ん？　何か言ったか？": "Hm? Em vừa nói gì à?",
    "い、いえ！　こっちの話です！": "K-Không có gì đâu ạ! Em tự nói một mình thôi!"
}

# ==========================================
# Ghi đè các file và kiểm tra
# ==========================================
print("Loaded Yuri Part 1")

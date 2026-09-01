# -*- coding: utf-8 -*-
import json
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(r"d:\idontknow\dotabyss-translation")
NOVELS_DIR = ROOT_DIR / "translations" / "novels"

translations = {}

# ==============================================================================
# HMR_10220100011 (Yuri 1 Intro)
# ==============================================================================
translations["hmr_10220100011"] = {
    "激しい雨音が洞窟の外で轟いている。<br>一歩先も見えない濃霧と、体温を奪い去る冷たい雨。": "Tiếng mưa dữ dội ầm ầm ngoài hang.<br>Màn sương mù dày đặc che khuất tầm nhìn và cơn mưa buốt giá.",
    "暗い洞窟の奥で、<user>とユーリの<br>ふたりの荒い吐息だけが重なり合うように響いていた――": "Sâu trong hang tối, chỉ còn lại tiếng thở dồn dập<br>của <user> và Yuri hòa quyện vào nhau――",
    "はぁ、はぁ……。<br>ここならば、ひとまず……雨風は凌げるはずだ。": "Hà... hà...<br>Ở đây tạm thời có thể tránh được mưa gió rồi.",
    "はぁ、はぁ……。<br>霧で皆さんの姿が見えなくなった時はどうなることかと思いました……": "Hà... hà... Lúc sương mù che khuất mọi người,<br>em cứ tưởng là có chuyện chẳng lành rồi chứ...",
    "ユーリの細い肩が小刻みに震えている。薄い生地の服は完全に張り付き、<br>彼女の瑞々しいボディラインを無防備に晒していた。": "Bờ vai mảnh mai của Yuri khẽ run. Lớp áo mỏng ướt sũng<br>để lộ những đường cong thiếu nữ nuột nà đầy gợi cảm.",
    "でも……これは、しばらく降りやみそうにないですね……。<br>天候が落ち着くまでは、この洞窟でじっとしていたほうがよさそうです。": "Nhưng... mưa thế này chắc chưa tạnh ngay đâu ạ...<br>Tốt nhất ta nên ở yên trong hang chờ thời tiết ổn định lại.",
    "確かにな。この大雨と濃霧の中で移動するのは危険だ。<br>いつ止むか分からないが、ここでしばらく休憩だな。": "Đúng vậy. Đi lại trong mưa to và sương mù thế này rất nguy hiểm.<br>Dù chưa biết khi nào tạnh, cứ tạm nghỉ ở đây đã.",
    "……あの、しれー。あ、あの……こんな時に不謹慎かもしれませんが、<br>ずっと、気になっていたことがあって……": "Tư lệnh ơi... Chuyện này lúc này có hơi không phải phép,<br>nhưng có một điều em cứ thắc mắc mãi...",
    "……なんだ？ <br>気を紛らわせるためだ、なんでも話してみろ。": "Chuyện gì thế?<br>Cứ nói đi, coi như để phân tán sự chú ý.",
    "……酒場の、２階のことです。夜、お食事をしていると、いつも、<br>綺麗なドレスを着た女性が、男の人と階段を上がっていきますよね。": "Là chuyện trên tầng hai quán rượu ạ. Mỗi tối lúc ăn cơm,<br>em luôn thấy gái mặc váy đẹp cùng đàn ông bước lên lầu.",
    "……あそこで、皆さんは何をされているのでしょうか？": "Ở trên đó... mọi người đang làm gì vậy ạ?",
    "あ～……あれはだな、男と女の大人のコミュニケーションというか……<br>つまり――": "À... đó là chuyện giao lưu người lớn giữa nam và nữ...<br>Nói tóm lại là――",
    "そ、そんなことをしていたのですか……！<br>……は、初めて知りました！": "H-Hóa ra là làm chuyện đó sao...!?<br>L-Lần đầu tiên em mới biết đấy ạ!",
    "まぁ、そういう大人の世界があるってことだ。": "Thì trên đời luôn có thế giới người lớn như vậy mà.",
    "た、確かに……わたしには未知の世界のお話でした……。<br>そっかぁ～……そんなことをされていたんですね……": "Đ-Đúng là một thế giới xa lạ với em...<br>Ra là vậy... Hóa ra họ làm chuyện đó ư...",
    "ユーリは、初めて知った『大人の世界』に、<br>赤面しながらも興奮しっぱなしの様子だ。": "Yuri đỏ bừng mặt khi biết đến 'thế giới người lớn',<br>nhưng vẻ mặt lại không giấu nổi sự phấn khích tò mò.",
    "あ、あの……！　その娼館っていう場所のこと、<br>もっと詳しく教えてもらえませんか……？": "A-Anh Tư lệnh...! Về nơi gọi là kỹ viện đó,<br>anh có thể kể cho em nghe chi tiết hơn được không...?",
    "ユーリは、娼館に興味津々のようで、<br>食い気味に質問を投げかけてくる。": "Yuri tỏ ra vô cùng hiếu kỳ về kỹ viện,<br>háo hức dồn dập đặt câu hỏi.",
    "あそこは客を満足させるためのプロの世界なんだ。<br>働くには、まずは俺との『研修』が必要でだな……": "Đó là nơi làm việc chuyên nghiệp để phục vụ khách.<br>Muốn làm ở đó thì trước tiên phải 'tập huấn' với anh đã...",
    "しれーと……け、けけっ、研修……っ！？<br>それは、その……あの方たちのようなことを、しれーと……？": "T-Tập huấn với anh Tư lệnh...!?<br>Tức là... làm chuyện giống như những người đó với anh...?",
    "ユーリは、そのまま押し黙ってしまう。<br>激しい雨音と、ユーリの心臓の鼓動が聞こえてきそうなほどの静寂――": "Yuri bỗng im bặt. Giữa tiếng mưa rào xối xả,<br>không gian tĩnh lặng tới mức nghe rõ cả tiếng tim cô đập――",
    "……は、はくしょんっ！<br>くそっ、この寒さは流石に堪えるな……": "Hắt... hắt xì!<br>Chết tiệt, lạnh thế này đúng là chịu không thấu...",
    "気温が下がってきたみたいですね……。<br>急いで火を起こしますね。": "Hình như nhiệt độ đang hạ thấp rồi...<br>Em sẽ đi nhóm lửa ngay.",
    "あと、濡れた服は脱いでしまった方がいいです。<br>このままだと体温を奪われてしまって危険です。": "Với lại, anh nên cởi đồ ướt ra đi ạ.<br>Cứ mặc thế này sẽ bị hạ thân nhiệt, nguy hiểm lắm.",
    "わ、分かった！<br>さすがにユーリは登山の知識が豊富だな。助かるよ。": "A-Anh hiểu rồi! Yuri am hiểu kiến thức leo núi thật.<br>Cảm ơn em nhiều nhé.",
    "（気温が低すぎる……着替えの服もないですし……。<br>このままじゃ、わたしもしれーも体温がどんどん下がっちゃって危険……）": "(Nhiệt độ thấp quá... lại không có đồ thay...<br>Cứ thế này cả hai đều bị hạ thân nhiệt mất...)",
    "（こういう時は……。<br>そ、そうだ……！　あの方法しかない……！）": "(Những lúc thế này...<br>Đ-Đúng rồi...! Chỉ còn cách đó thôi...!)",
    "濡れた服を脱いでいると、<br>何やら意を決した表情のユーリが静かにこちらに近づいてくる。": "Trong lúc tôi đang cởi quần áo ướt,<br>Yuri với nét mặt đầy quyết tâm bỗng lặng lẽ tiến lại gần.",
    "あ、あの……このままだとふたりとも体温が低下して危険です。<br>だ、だから、その……し、失礼しますっ！": "A-Anh ơi... Cứ thế này cả hai sẽ bị hạ thân nhiệt mất.<br>V-Vì thế, ừm... x-xin thất lễ ạ!"
}

# ==============================================================================
# HMR_10220100012 (Yuri 1 H-scene)
# ==============================================================================
translations["hmr_10220100012"] = {
    "ユーリのきめ細やかな肌が吸い付くように密着し、触れ合っている部分から、<br>熱すぎるほどの体温が溶け出して伝わってくる。": "Làn da mịn màng của Yuri áp sát vào người tôi,<br>từng điểm chạm truyền sang hơi ấm nóng hổi.",
    "……驚かせて、すみません。でも、体温を下げずに保つには、<br>こうして人肌同士で温め合うのが、最も効率的なんです……": "...Làm anh giật mình, em xin lỗi. Nhưng để giữ ấm cơ thể,<br>da kề da sưởi ấm cho nhau thế này là hiệu quả nhất...",
    "毅然とした口調を保とうとしているが、こちらに押し当てられた<br>彼女の心臓は、壊れた鐘のように激しく脈打っていた。": "Dù cố giữ bình tĩnh, trái tim cô đang áp vào ngực tôi<br>lại đập thình thịch như một chiếc chuông vỡ.",
    "ど、どうですか、しれー……？<br>……温かい、ですか……？": "A-Anh thấy thế nào, anh Tư lệnh...?<br>...Có thấy ấm không ạ...?",
    "――ユーリとこうしてると、すごく温かい……<br>そう答える。": "――Ở cạnh Yuri thế này ấm áp lắm...<br>Tôi khẽ đáp.",
    "よかったです……しれーを遭難させた上に風邪までひかせちゃったら、<br>山の案内役として失格ですから。": "Thế thì tốt quá... Để anh gặp nạn lại còn bị cảm lạnh,<br>thì em không xứng làm người dẫn đường leo núi nữa rồi.",
    "義務感を口にする彼女だが、ふと、このあまりにも手慣れた様子が気になり、<br>――こういう救助はよくあるのか？　と問いかけてみる。": "Nghe cô nói vì trách nhiệm, tôi tò mò trước cử chỉ thành thục này,<br>――liền hỏi xem cách cứu hộ này có thường xảy ra không.",
    "い、いえ！　知識として知っていただけですっ！　実践は初めてですし、<br>それに……相手が誰でもいいってわけじゃないですよ……": "K-Không đâu ạ! Em chỉ biết lý thuyết thôi! Đây là lần đầu thực hành,<br>với lại... đâu phải với ai em cũng làm thế này...",
    "俺が相手ならいいのか……？<br>――そうたずねる。": "Nếu là anh thì được sao...?<br>――Tôi hỏi lại.",
    "……はい。しれーが相手なら……。<br>えっ……あ、あの……": "...Vâng. Nếu là anh Tư lệnh thì...<br>Ủa... ơ, anh ơi...",
    "肯定の返事を聞いた瞬間、<user>の理性は、<br>彼女の濡れた髪から漂う濃密な香りに奪われてしまう。": "Ngay khi nghe câu đồng ý, lý trí của <user><br>đã bị hương thơm ngạt ngào từ mái tóc ướt của cô cướp mất.",
    "その細い首元に鼻先を埋める。雨に濡れた髪の清涼感。<br>そして、その奥から立ち上る、若々しい女性特有の甘く芳しい体臭――": "Tôi vùi mũi vào chiếc cổ thon. Vị thanh mát của tóc ướt,<br>hòa cùng mùi hương cơ thể thiếu nữ ngọt ngào quyến rũ――",
    "し、しれー……どうしたんですか？　そ、そんなにクンクンしないで<br>くださいよぉ……さっき走った時に、汗かいちゃってますからぁ……": "A-Anh Tư lệnh... anh sao thế? Đ-Đừng có hít hà như thế mà...<br>Lúc nãy chạy vội, em đổ mồ hôi rồi đấy ạ...",
    "――汗を掻いてるのはお互い様だ。でも、ユーリのはいい匂いだ……<br>そう耳元で囁く。": "――Cả hai ta đều đổ mồ hôi mà. Nhưng của Yuri thơm lắm...<br>Tôi thì thầm bên tai cô.",
    "そ、そんなこと……な、なんか恥ずかしいですよ……。<br>でも……わたしも、しれーの匂い……好きな匂いです……": "C-Chuyện đó... ngượng chết đi được...<br>Nhưng... em cũng... rất thích mùi hương của anh...",
    "重なり合った体温と、首筋から立ち上る酔いしれるような甘い香りに、<br>抑え込んでいた興奮が、抗いようもなく掻き立てられていく。": "Hơi ấm hòa quyện cùng hương thơm say đắm nơi cần cổ<br>đã thổi bùng dục vọng kìm nén không thể cưỡng lại.",
    "あっ……んぅ……っ♡": "A... ưm...♡",
    "彼女の白い首筋に、熱い舌を這わせ、<br>湧き上がる欲情を押さえられず、腰を動かし始める。": "Tôi lướt đầu lưỡi nóng rực lên chiếc cổ trắng nõn,<br>không kiềm chế được ham muốn mà bắt đầu đưa đẩy hông.",
    "んっ、ふあぁ……く、くすぐったいです……あっ、はぁぁっ……": "Ưm, a... nh-nhột quá anh ơi... a, hà...",
    "少女特有のきめ細かい肌の質感に興奮が臨界点を超え、<br>熱く屹立した肉棒が、彼女の無防備な陰唇を熱く擦り上げていく。": "Làn da thiếu nữ mịn màng khiến cơn hưng phấn vượt giới hạn,<br>thanh thịt cương cứng nóng hổi cọ xát vào môi dưới không phòng bị.",
    "ちょ、ちょっと……ま、待って……！<br>しれーの硬いのが……あ、当たってますぅ～！": "K-Khoan đã... ch-chờ chút...!<br>Cái vật cứng của anh... đ-đang cạ trúng em rồi...!",
    "擦れ合う肉棒と膣口の摩擦が急に緩くなる。<br>ユーリの愛蜜が溢れ出し、それが潤滑油となったのだった。": "Sự ma sát giữa thanh thịt và cửa mình bỗng trơn tru hẳn.<br>Dâm dịch ngọt ngào của Yuri tuôn ra, đóng vai trò như chất bôi trơn.",
    "ま、待って……しれー！　こ、興奮しすぎですよぉ～～～っ！<br>はぁっ、はぁっ……ん、んんっ……！": "K-Khoan đã... anh Tư lệnh! A-Anh hưng phấn quá rồi đóoo!<br>Hà, hà... ưm, ưm...!",
    "潤みきった瞳と、甘い蜜にまみれた感触がさらに興奮を掻き立てる。<br>滑りの良さに任せて、さらに深く、強く腰を叩きつけていく。": "Đôi mắt ngấn lệ cùng mật ngọt ướt đẫm kích thích cơn dục vọng.<br>Nhờ sự trơn ướt, tôi thúc hông mạnh mẽ và sâu hơn nữa.",
    "はっ、ぁっ、んぅ～～っ……あっ、ふっ……": "Hà, a, ưm... a, phù...",
    "必死に声を抑えようとして、けれど抑えきれなかった喘ぎ声が洞窟に甘く響く。<br>愛液は肉棒を濡らし、どんどん滑りをよくしていく。": "Tiếng rên rỉ kiềm nén nhưng không thể vang vọng khắp hang.<br>Dâm dịch thấm đẫm thanh thịt, khiến từng cú đẩy càng trơn tru.",
    "と――思っていた以上に滑りがよかったらしく、<br>腰を動かした拍子に肉棒が大きく滑り、亀頭が膣口に当たり――": "Và rồi―― do trơn hơn tưởng tượng, một cú nhấp hông đã làm<br>thanh thịt trượt đi, quy đầu thúc thẳng vào cửa mình――",
    "んっぐ！？　あぁっ！　はぁぁああぁ～～～ッ……！！！": "Ưm...!? Aaa! Haaa...!!!",
    "愛液の潤滑を借りた肉棒は、何の抵抗もなくユーリの狭い入り口を押し開き、<br>そのままの勢いで処女の証を一気に貫いてしまったのだ。": "Nhờ dâm dịch bôi trơn, thanh thịt dễ dàng tách mở lối vào,<br>thừa thắng xông lên đâm thủng màng trinh của Yuri trong một nhịp.",
    "あっ、ちょ、ちょっと待ってぇ……！<br>これっ、は、入っちゃってますよぅっ！　はうっ……！": "A, kh-khoan đã nào...!<br>Cái này, đ-đút vào trong mất rồi! Hức...!",
    "突き破られた衝撃と、異物に満たされる異様な感覚に、<br>ユーリは目を白黒させて絶句する。": "Cảm giác bị đâm thủng và dị vật lấp đầy bên trong<br>khiến Yuri trợn tròn mắt, kinh ngạc không thốt nên lời.",
    "しかし理性を完全に溶かされた今、<br>湧き上がる欲情を止めることなどできなかった。": "Thế nhưng khi lý trí đã hoàn toàn tan chảy,<br>tôi chẳng thể nào kìm hãm dục vọng đang cuộn trào được nữa.",
    "あっ……！　んっ、はあぁ……っ！": "A...! Ưm, haaa...!",
    "溢れ出す欲情をぶつけるように、下から力強く腰を突き上げ始める。<br>肉と肉が激しく衝突する度に、湿った衝撃音が洞窟の壁に低く反響していく。": "Như muốn trút hết ham muốn, tôi thúc mạnh hông từ bên dưới.<br>Mỗi lần va chạm dữ dội, tiếng bì bạch vang vọng khắp vách hang.",
    "はぁっ……あぁっ、んっ、やっ……！<br>し、しれー……っ！": "Hà... a, ưm, đừng mà...!<br>A-Anh Tư lệnh...!",
    "一突きごとに最奥を抉られ、ユーリの口からは、<br>もはや言葉にならない、ひきつったような嬌声があふれ出した。": "Mỗi cú thúc đều chạm tới tận cùng, từ miệng Yuri<br>bật ra những tiếng rên kiều mị nghẹn ngào không thành lời.",
    "あ、ぁぐっ……！？<br>ひ、ひゃあぁ……っ、ん、んぅううっ……！！": "A, ưm...!?<br>H-Hyaaa... ưm, ưm...!!",
    "内壁は侵入者を拒むどころか、吸い付くような熱を帯びて肉棒の形状をなぞり、<br>とろけるような粘膜の愛撫を返してくる。": "Thành âm đạo chẳng hề cự tuyệt, mà siết chặt lấy thanh thịt,<br>như dùng lớp niêm mạc mềm mại đáp lại từng nhịp yêu thương.",
    "んっ……んっ……あぁっ……ふあっ……！<br>あぁっ……やっ……！　はっ、あぁん……！": "Ưm... ưm... a... phù...!<br>A... đừng mà...! Hà, a...!",
    "突き上げられるたび、彼女の身体は弓なりに反り、<br>上体を揺らしながら、その激しい衝撃に耐え忍んでいた――": "Mỗi lần bị thúc lên, cơ thể cô uốn cong như cánh cung,<br>thân trên rung lắc dữ dội đón nhận từng đợt va chạm――",
    "し……しれー……！<br>こ、これ……き、気持ち……いい……！　あっ……あはぁぁっ！": "A-Anh Tư lệnh...!<br>C-Cái này... s-sướng... quá...! A... aaaa!",
    "いつしかユーリの身体から強張りは消え、快楽の奔流に身を委ね始めていた。<br>そのとき――": "Sự căng thẳng trên người Yuri dần tan biến, cô bắt đầu thả mình<br>vào dòng thác khoái lạc. Đúng lúc đó――",
    "えっ……！？　そ、そんな……な、何これぇ……！<br>勝手に腰、動いちゃう……はンっ……！　あっ、ひゃっ、んぅ……！": "Eh...!? S-Sao lại thế... c-cái gì thế này...!<br>Eo em tự chuyển động mất rồi... a...! A, ưm...!",
    "いつしか、ユーリは自分で腰を振っていた。<br>本能に身を任せ、快感を求めるように自ら腰を艶めかしく動かしている。": "Chẳng biết từ lúc nào, Yuri đã tự lắc lư hông.<br>Theo bản năng, cô chủ động đưa đẩy đầy mời gọi để tìm khoái cảm.",
    "あっ……ぅうんっ……はぁあぁっ！<br>やっ……！　き、気持ち良すぎて……止まんない……！　はぁぁっ！": "A... ưm... haaa!<br>Đừng mà...! S-Sướng quá... không dừng lại được...! Haaa!",
    "自分でも制御できない、本能的な腰の動き。積極的に快楽を貪ろうとする<br>自分の身体に、誰よりもユーリ自身が驚愕していた。": "Chính Yuri là người kinh ngạc nhất trước cơ thể mình,<br>khi chiếc hông cứ tự động đưa đẩy thèm khát khoái lạc.",
    "（やだ……！　しれーの前で、こんなに腰振って……恥ずかしいよぅ……！<br>わたし、こんなにエッチな子だったの……！？）": "(Trời ơi...! Trước mặt anh mà mình lắc hông thế này... xấu hổ quá!<br>Hóa ra mình lại là đứa con gái dâm đãng thế này sao...!?)",
    "ご、ごめんなさい……！<br>わたしばっかり、勝手に動いちゃって……あっ、はぁっ……！": "E-Em xin lỗi...!<br>Cứ tự ý chuyển động một mình thế này... a, hà...!",
    "不安そうなユーリに、すごく気持ちいいから大丈夫だと答える。<br>実際、締まったり緩めたりと、緩急のある刺激が何とも言えず気持ちいい。": "Thấy Yuri lo lắng, tôi bảo rằng em làm thế anh sướng lắm.<br>Thực sự những nhịp siết nhả bên trong cô bé sướng không tả xiết.",
    "ほんとうですか……？　よかった……。<br>しれー……あの、わたし……このまましれーと気持ち良くなりたいです……": "Thật ạ...? May quá...<br>Anh Tư lệnh ơi... em... muốn cùng anh sướng như thế này tiếp...",
    "だから……最後まで、お願いします。": "Vì thế... xin anh hãy làm tới cùng nhé.",
    "誘うように潤んだ瞳で見つめられ、<br>肉棒がさらに一段階、太く滾っていく。": "Trước ánh mắt đẫm lệ đầy mời gọi ấy,<br>thanh thịt của tôi lại trướng to và nóng rực thêm một bậc.",
    "ひゃぅ……っ！　ああっ、はあぁっ、ぁああ～～～っ……！": "Hyaaa...! Aaa, haaa...!",
    "激しく腰を突き上げるたび、ぎちぎちに張り詰めた肉棒が、<br>ユーリの最奥――子宮の入り口を幾度も力強く叩き上げていく。": "Mỗi cú thúc dữ dội, thanh thịt căng cứng như sắt thép<br>lại liên hồi nện thẳng vào nơi sâu nhất―― tử cung của Yuri.",
    "わっ、あぁあっ、はぅっっ……！　こ、これ、すごいっ、すごいですぅ～……！<br>わ、わたしも動きます、ね……しれーを、気持ち良くして、あげなきゃ……！": "Oa, aaa, hức...! C-Cái này tuyệt quá đi mất...!\nE-Em cũng sẽ chuyển động... phải làm cho anh sướng nữa chứ...!",
    "一突きごとに脳髄を焼くような衝撃が走り、<br>ユーリの視界は快楽の火花で白く塗り潰されていく。": "Mỗi nhịp đâm là một luồng điện xé toạc tâm trí,<br>tầm nhìn của Yuri bị pháo hoa của sung sướng nhuộm trắng xóa.",
    "あっ、ひっ、はっっ、ひゃうっ……！　あっ、あぁっ、あぁ～～～……っ！<br>も、もう、だめぇ……頭、ボーっとしてきて、くらくらしちゃいますぅ～……！": "A, hức, hà, a...! A, a, aaa...!\nK-Không được rồi... đầu óc em quay cuồng trống rỗng hết rồi...!",
    "ユーリの膣壁がビクビクと蠕動し始める。絶頂が近いようだ。<br>とはいえ、限界が近いのはこちらも同じだった。": "Âm đạo của Yuri co giật kịch liệt. Có vẻ cô sắp lên đỉnh.<br>Tuy nhiên, tôi cũng đã sắp chạm đến giới hạn.",
    "しれぇ……あっ、やっ……も、もう、わたし……！<br>ひあっ、はっ、あっ、あっっ……！": "Anh Tư lệnh ơi... a, đừng mà... em sắp...!\nA, hà, a, a...!",
    "あっ、あっ、だ、だめぇっ！　ぁああぁぁ～～～ッ！！！": "A, a, k-không được rồi! Aaaaa...!!!",
    "絶頂の瞬間、ユーリの身体はビクンビクンと激しく痙攣し、<br>その震える最奥へと熱く濃密な精液が大量に注ぎ込まれていく。": "Khoảnh khắc lên đỉnh, thân thể Yuri giật bắn co thắt dữ dội,<br>dòng tinh dịch nóng hổi đặc quánh bắn xối xả vào nơi sâu nhất.",
    "はぁ、はぁ……はぁ……": "Hà... hà... hà...",
    "静まり返った洞窟に、ふたりの荒い呼吸だけが重なり合う。<br>絶頂の余韻に浸りながら、息を整え、徐々に冷静さを取り戻していくユーリ。": "Trong hang động yên ắng, chỉ còn tiếng thở dốc của hai người.<br>Chìm trong dư âm cực khoái, Yuri dần lấy lại hơi thở và bình tĩnh.",
    "（わ、わたし……エッチ、しちゃったんだ……しれーと……！）": "(M-Mình... đã làm chuyện ấy rồi... với anh Tư lệnh...!)",
    "冷静になるにつれ、羞恥心がじわじわと込み上げてくる。<br>ユーリは不安げな瞳でこちらを見つめると、震える声で問いかけた。": "Khi bình tâm lại, cảm giác xấu hổ trào dâng.<br>Yuri nhìn tôi với ánh mắt bồn chồn rồi run run cất tiếng hỏi.",
    "し、しれー……わ、わたし、自分であんなに腰振っちゃって……、<br>変な女の子だと……エ、エッチな女の子だと思っちゃいましたよね……？": "A-Anh ơi... em tự lắc hông nhiều như thế...<br>Anh có thấy em là đứa con gái kỳ lạ... d-dâm đãng không ạ...?",
    "不安そうに一気に言うユーリに、思わず笑みがこぼれる。<br>そんなことないぞ。むしろ、こっちも夢中になってしまったしな――と答える。": "Thấy Yuri lo lắng nói một tràng, tôi bật cười trấn an.<br>Làm gì có chuyện đó, chính anh cũng mê mẩn em đấy thôi―― tôi đáp.",
    "それって、あ、あの……。<br>わたしとエッチなことして、よかったってことですか……？": "Thế tức là, ừm...<br>Làm chuyện ấy với em... anh thấy thích lắm đúng không ạ...?",
    "もちろんだ――と力強く頷いて答えてやる。": "Tất nhiên rồi―― tôi gật đầu quả quyết.",
    "その言葉を聞いたユーリは、張り詰めていた表情をふっと和らげると、<br>どこか安堵したような、慈愛に満ちた柔らかな微笑みを浮かべる。": "Nghe thế, nét mặt căng thẳng của Yuri dịu lại,<br>nở nụ cười hiền từ, ngập tràn sự an tâm và yêu thương.",
    "……。<br>……よかった……": "...<br>...May quá rồi..."
}

# ==============================================================================
# HMR_10220100013 (Yuri 1 Epilogue)
# ==============================================================================
translations["hmr_10220100013"] = {
    "洞窟の外を支配していた猛烈な雨音は、いつの間にか止んでいた。<br>岩の隙間から差し込む太陽の光が、湿った地面をキラキラと照らしている。": "Tiếng mưa rào dữ dội ngoài hang đã tạnh từ lúc nào.<br>Tia nắng rọi qua kẽ đá, chiếu sáng nền đất ẩm ướt lấp lánh.",
    "すっかり天気もよくなりましたね。": "Thời tiết đã đẹp trở lại rồi ạ.",
    "ああ。だが、早いところ帰還しないとな。<br>遭難したと思われて、捜索隊が出ているかもしれない。": "Ừ. Nhưng ta phải mau chóng trở về thôi.<br>Mọi người tưởng ta gặp nạn có khi đang cử đội tìm kiếm rồi.",
    "あ、あの……本当に、わたしのこと、<br>エッチな女の子だと思ってません……よね？": "A-Anh ơi... anh thực sự không nghĩ em<br>là đứa con gái dâm đãng đấy chứ...?",
    "ユーリは、昨夜の自分が見せた積極的な振る舞いを思い出し、<br>顔を赤らめて俯いてしまう。": "Yuri nhớ lại những hành động chủ động tối qua,<br>mặt đỏ bừng bối rối cúi gằm xuống.",
    "ふ、普段からエッチなわけじゃないんですよ？　そ、その……神殿で育った<br>ものですから、そこでの戒律が結構厳しくて、そ、その反動というか……": "B-Bình thường em không thế đâu ạ! Em lớn lên ở thần điện,<br>giới luật khắt khe quá nên... có lẽ là bị dồn nén...",
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

# ==============================================================================
# HMR_10220100021 (Yuri 2 Intro)
# ==============================================================================
translations["hmr_10220100021"] = {
    "あの晩、<user>との初体験で自分の未熟さを痛感した<br>ユーリは、大好きな”しれー”をもっと気持ち良くさせたいと決意する。": "Đêm đó, sau lần đầu ân ái cảm thấy bản thân còn vụng về,<br>Yuri quyết tâm phải làm cho anh Tư lệnh sướng hơn nữa.",
    "ユーリは、あろうことか自ら娼館の門を叩く。すべては最愛の人に<br>最高のもてなしを提供するための、彼女なりの”聖務”としての決断だった。": "Yuri đã tự mình gõ cửa kỹ viện. Tất cả là vì muốn dâng hiến<br>những điều tuyệt nhất cho người mình yêu như một 'thánh vụ'.",
    "そして今日、娼館の一室で、ユーリは初めての客を迎え、<br>彼女なりのやり方で接客を開始する――": "Và hôm nay, trong căn phòng kỹ viện, Yuri đón vị khách đầu tiên,<br>bắt đầu tiếp đãi theo cách rất riêng của mình――",
    "……はぁ。実は今度、山の頂に出没するモンスターの調査隊に<br>抜擢されちゃってね。正直、登山の経験なんてあんまりないから不安なんだ。": "Haizz. Tôi vừa được chọn vào đội khảo sát quái vật trên đỉnh núi.<br>Nói thật là ít kinh nghiệm leo núi nên lo quá.",
    "登山についてなら、わたしは詳しいですよ。なにせ、山生まれの山育ちですし、<br>それにミレスガルド騎士団の山岳訓練にだって同行してますからねっ。": "Về leo núi thì em rành lắm. Em sinh ra và lớn lên ở núi rừng,<br>lại từng đi theo huấn luyện vùng núi của kỵ sĩ đoàn Milesgard nữa.",
    "それは心強いな……。かなりの標高まで登るらしくて、テントや寝袋、<br>それに食糧……相当な重量の荷物を運ぶことになるらしいんだ。": "Nghe yên tâm hẳn... Phải leo lên độ cao lớn, lều bạt, túi ngủ,<br>lại thêm lương thực... vác hành lý nặng lắm.",
    "うーん、荷物は詰めかたや背負いかたで、疲労がまったく違いますからね。<br>お客さんの仰る装備なら、大体わたしと同じくらいの重さになりそうですね。": "Cách sắp xếp và đeo hành lý ảnh hưởng rất nhiều đến thể lực.<br>Số trang bị anh nói chắc nặng cỡ bằng người em đó ạ.",
    "……君と同じくらい？<br>それなら、どれくらいの重さなのか試しに抱き上げてみてもいいかな？": "...Nặng bằng em sao?<br>Vậy tôi thử bế em lên xem cảm giác nặng thế nào được không?",
    "フフ、いいですよ。ですが……抱え上げるだけなら簡単です。実際の山道では、<br>その重さを支えて歩き続ける強靭な足腰が必要になりますから……": "Hi hi, được chứ. Nhưng chỉ bế lên thì dễ lắm. Đường núi thực tế<br>đòi hỏi đôi chân và hông dẻo dai để đi liên tục...",
    "それだとあまり参考にならないかもです。抱えるだけなら簡単ですが、<br>山では荷物を抱えたまま歩き続けなきゃいけないので。": "Chỉ bế không thì khó hình dung lắm. Vì trên núi<br>phải vừa ôm vác hành lý vừa liên tục sải bước mà.",
    "……そうだ。それなら、わたしを使って足腰の鍛錬、してみます？": "...Đúng rồi. Hay anh dùng em để luyện tập thể lực hông và chân nhé?",
    "君を使って……？": "Dùng em để luyện tập...?",
    "はい。試しにやってみましょう！": "Vâng ạ. Ta thử làm xem sao nhé!"
}

# ==============================================================================
# HMR_10220100022 (Yuri 2 H-scene)
# ==============================================================================
translations["hmr_10220100022"] = {
    "（な、なんですか、この格好……っ！？　アソコが丸見えだし……<br>それに、お客さんの熱いのが、あんなに近くに……っ！）": "(T-Tư thế gì thế này...!? Chỗ đó bị nhìn thấy hết trơn...<br>Lại còn thứ nóng rực của khách ở sát sạt thế này...!)",
    "正面に据えられた大きな鏡には、男の腕に太ももを掴まれ、<br>無防備に股を開かされた自分の姿が、隅々まで鮮明に映し出されている。": "Chiếc gương lớn phản chiếu rõ thân thể cô đang bị giữ chặt đùi<br>và banh rộng hai chân ra không chút phòng bị.",
    "（あ、あれ……？　山岳訓練の為に提案したはずなのに……<br>な、なんかとんでもなく恥ずかしい体勢になってしまってるような……）": "(Ủ-Ủa...? Mình rõ ràng đề xuất để luyện tập leo núi mà...<br>s-sao lại thành ra cái tư thế ngượng chín người thế này...)",
    "あ、あの……やっぱり、この体勢はちょっと……": "A-Anh ơi... tư thế này quả nhiên có hơi...",
    "あまりの羞恥心に体勢を変えることを提案しようとするが、<br>男は鼻息荒く、そのまま行為をしたいと提案してくる。": "Vì quá ngượng nên cô định đổi tư thế,<br>nhưng gã đàn ông thở dồn dập, muốn cứ thế mà làm tới.",
    "え？　え？<br>こ、このまま……しちゃうんですかっ！？": "Eh? Eh?<br>C-Cứ để thế này... mà làm luôn sao ạ!?",
    "はぁぁっ……！　あっ……やっ……ちょ、ちょっと……！": "Haaa...! A... đừng mà... ch-chờ chút...!",
    "止める間もなく、男は腰を動かしてユーリの膣口に陰茎をこすりつけ始める。<br>敏感な部位を擦られ、ユーリは漏れそうになる声を咄嗟に飲み込む。": "Không kịp cản, gã đàn ông chà xát dương vật lên cửa mình Yuri.<br>Bị cọ xát nơi nhạy cảm, Yuri vội nuốt tiếng rên vào trong.",
    "んっ……ふっ、んっ……はっ、ぁくっ……": "Ưm... phù, ưm... hà, hức...",
    "声は必死にこらえていたが、身体の反応までは抑えることができない。<br>ユーリの秘所は徐々に濡れ、潤いを増していく。": "Dù cố kìm nén tiếng rên nhưng cơ thể cô chẳng thể dối lừa.<br>Nơi thầm kín của Yuri dần ướt đẫm, dâm dịch tiết ra ngày một nhiều.",
    "はぁぁっ……ふっ、あぁぁっ……": "Haaa... phù, aaaa...",
    "男の腰の動きが大きくなり、長いストロークでユーリの敏感な部位を<br>擦り上げていく。日頃鍛錬に励んでいるのだろう。体力が尽きる様子はない。": "Nhịp hông của gã miết dài qua vùng nhạy cảm của Yuri.<br>Nhờ hay rèn luyện nên gã chẳng có vẻ gì là đuối sức.",
    "あっ、はぁぁっ～……ゃんっ！<br>あ、あのっ……も、もうちょっと、落ちついて……": "A, haaa... a nhược!<br>A-Anh ơi... b-bình tĩnh lại chút đã...",
    "激化する摩擦に、ユーリは自制を食い破られ声を漏らす。<br>翻弄され揺れる身体から溢れる甘い悲鳴が、男の欲情を激しく煽っていく。": "Ma sát mãnh liệt khiến Yuri không kìm được tiếng rên.<br>Những tiếng kêu ngọt ngào càng thổi bùng dục vọng của gã đàn ông.",
    "あっ、はぁぁ……っ、んっ、ひぅぅっ……ふあっ、あっ、はぁぁ……っ！": "A, haaa... ưm, hức... a, haaa...!",
    "小ぶりな乳房が、激しく揺さぶられる度に震え、鏡の中で淫らに波打つ。<br>その淫靡な姿に、男の陰茎は天を突くように角度を上げ――": "Cặp tuyết lê nhỏ nhắn nảy lên dập dềnh trong gương.<br>Hình ảnh dâm mỹ đó khiến dương vật gã đàn ông ngóc cao hơn nữa――",
    "え？　ちょっ……！？　えっ！？　えぇぇ～～～っ！？": "Eh? Khoan đã...!? Eh!? Ehhh...!?",
    "勢い余って愛液で滑った陰茎がユーリの膣口を押し開き、<br>その中に潜り込んでしまったのだ。": "Do trơn trượt bởi dâm dịch, thanh thịt đã tách mở cửa mình Yuri<br>và trượt thẳng vào sâu bên trong.",
    "その状況に気が付いた客の男は、慌てて謝罪する。<br>――す、すみませんっ！　興奮してしまって……": "Nhận ra tình huống, vị khách luống cuống xin lỗi:<br>――X-Xin lỗi em! Tôi hưng phấn quá...",
    "だ、大丈夫です……急に挿れられて、<br>びっくりしちゃっただけですから……": "K-Không sao đâu ạ... Em chỉ giật mình<br>vì bị đút vào bất ngờ thôi...",
    "ふぅ……ふぅぅ……どうぞ、このまま続けてください。<br>……これは、険しい山道を登るための鍛練ですから。": "Phù... phù... Xin anh cứ tiếp tục thế này đi ạ.<br>...Dù sao đây cũng là bài luyện tập vượt đường núi mà.",
    "ユーリの優しい言葉に、客の男は安心する。<br>肉棒に伝わる柔らかな誘惑に、欲情が湧き上がって来る。": "Lời nói dịu dàng của Yuri làm gã yên tâm.<br>Sự mềm mại ôm siết lấy thanh thịt khiến dục vọng bùng cháy.",
    "あっ、はぁあっ、あっ、やぅっ……！　んっ、あっ、あぁっ……！": "A, haaa, a, đừng mà...! Ưm, a, aaaa...!",
    "突き上げられる衝撃にユーリは身を震わせる。亀頭が子宮口を直接叩くたび、<br>彼女の口からは本能的な喘ぎが漏れ出す。": "Yuri run rẩy trước những cú thúc mạnh mẽ. Quy đầu nện vào tử cung,<br>tiếng thở dốc bản năng lại bật ra khỏi bờ môi cô.",
    "鏡に映る、快楽に頬を染め、視線の泳がせる自分の姿。<br>そのあまりの淫らさに、彼女の頭の中にある疑念が湧き上がる。": "Nhìn bóng mình trong gương với đôi má ửng hồng vì khoái lạc,<br>sự dâm đãng ấy khiến trong đầu cô nảy sinh mối hoài nghi.",
    "（あぁ……わたしって、感じてる時こんな淫らな顔してるんだ……。<br>……わたし、本当はエッチが大好きな淫らな女の子なのかな……？）": "(A... hóa ra khi sướng mình lại dâm đãng thế này...<br>...Phải chăng mình thực sự là đứa con gái nghiện làm tình...?)",
    "疑念とは裏腹に、子宮の奥からは溢れんばかりの愛液が湧き出す。<br>己の身体の正直な反応に、ユーリはついに自制心を投げ出してしまう。": "Trái với suy nghĩ ấy, dâm dịch từ tử cung cứ trào ra như suối.<br>Trước phản ứng của cơ thể, Yuri buông bỏ mọi sự kiềm chế.",
    "も、もっと……もっと、激しくしてください……！": "X-Xin anh... hãy làm mạnh hơn nữa đi ạ...!",
    "いっっ！？　あっっ、はぁっ、やぁっ……あっ、んぅ、ひあぁ……！": "A...!? A, haaa, đừng mà... a, ưm, aaa...!",
    "自分の口から出た思いがけない言葉にハッとする間もなく、<br>男の腰の動きが大きくなり、肉棒による刺激は激しさを増す。": "Chưa kịp ngỡ ngàng trước lời thốt ra từ chính miệng mình,<br>nhịp thúc của gã đàn ông đã dồn dập, kích thích dữ dội hơn.",
    "はぁぁんっ……！　あぁぁっ……ぅうんっ……はぁぁっ！<br>す、凄い……これっ！": "Haaa...! Aaa... ưm... haaa!<br>T-Tuyệt quá... cái này...!",
    "ユーリの求めを受け、男は欲望のままに肉棒を突き上げる。<br>より硬く、より太くなった肉棒に膣を刺激され、ユーリを更なる快楽が襲う。": "Được Yuri yêu cầu, gã thúc mạnh thanh thịt theo bản năng.<br>Thanh thịt ngày càng cương to đẩy Yuri vào cơn mê muội.",
    "（お客さんのアレ、わたしの一番気持ちいいところに当たってる……！<br>このままじゃあ……このままじゃあ……！）": "(Thứ của khách... đâm trúng chỗ sướng nhất của mình...!\nCứ thế này thì... cứ thế này thì...!)",
    "あぁあっ！　あっ、はんっ！　い、いいですぅ……！<br>気持ち、良すぎてぇ……あ、頭、真っ白になりますぅ……！": "Aaa! A, haaa! T-Tuyệt quá...!\nSướng quá rồi... đầu óc em trắng xóa hết rồi...!",
    "激しい揺さぶりに、頭の中までかき回されているような気分になる。<br>極限の快楽に、うまく思考できない。": "Những chấn động kịch liệt khiến tâm trí cô như bị khuấy đảo.<br>Khoái cảm cực hạn làm cô không thể suy nghĩ được gì nữa.",
    "ひぅぅ……！　あ、だ、だめ……っ、い、イキそう、です……！<br>わたし、イっちゃうかもですぅ～～……っ！": "Hức...! A, k-không được rồi... e-em sắp ra rồi...!\nEm... em sắp lên đỉnh mất rồi...!",
    "ユーリの膣がビクビクと収縮する。<br>その蠕動が男の射精感をも高まらせ、最後のスパートがかかる。": "Âm đạo của Yuri co thắt giật giật từng cơn.<br>Sự mút chặt ấy kích thích khoái cảm xuất tinh của gã lên tột cùng.",
    "イク……っ、イっちゃいますぅ～！<br>イク、イクイクっ、イっちゃうぅぅぅ～～……！": "Ra... em ra đâyyy!\nRa, em lên đỉnh đâyyy...!",
    "はぁあぁぁぁっ……！　ぁはぁぁ～～～～ッ！": "Haaaaaa...! Aaaaaa...!",
    "ユーリの顎が跳ね上がり、激しい痙攣と共に絶頂が訪れる。<br>その瞬間、大量の白濁液がユーリの膣内へと勢いよく流し込まれていく。": "Yuri ngửa cổ đón nhận cực khoái cùng những đợt co giật kịch liệt.<br>Đúng lúc đó, tinh dịch trắng đục bắn xối xả vào trong âm đạo cô.",
    "はぁあぁ……んっ、ふぁっ……。<br>お腹の中……まだ、いっぱい出てます……すごい……": "Haaa... ưm, phù...<br>Bên trong bụng em... vẫn bắn ra nhiều quá... tuyệt thật...",
    "膣内を熱い精液で満たされていく快感。<br>それと同時にユーリは客との”訓練”が無事終了したことに安堵する。": "Cảm giác âm đạo ngập tràn tinh dịch nóng hổi thật sung sướng.<br>Đồng thời Yuri thở phào vì buổi 'luyện tập' đã xong xuôi.",
    "はぁぁ～……お腹の中……あったかい……": "Haaa~... bên trong bụng... ấm áp quá...",
    "注ぎ込まれる精液の熱にうっとりと目を細めるユーリ。<br>しかし、これで訓練が終わると思っていた彼女の予想は、無情にも裏切られる。": "Yuri say đắm híp mắt tận hưởng hơi ấm của dòng tinh dịch.<br>Thế nhưng mong muốn buổi tập kết thúc đã bị dập tắt phũ phàng.",
    "えっ！？　ちょっ……ちょっと待ってください！！": "Eh!? Khoan... khoan đã anh ơi!!",
    "収まるどころか、再び硬度を増した肉棒が、<br>絶頂の余韻に震える彼女の膣内を再び蹂躙し始めたのだ。": "Chẳng những không xìu, thanh thịt lại cương cứng trở lại,<br>tiếp tục giày xéo bên trong âm đạo vẫn còn đang run rẩy.",
    "あっ、まっ、待ってぇ……！<br>こ、こんなの……わたしの身体がもたないってばぁっ！　ひうっ！？": "A, ch-chờ chút đã...!<br>Thế này... cơ thể em không chịu nổi đâu mà! Hya!?",
    "涙目でユーリが主張するも、火がついた男を止めることはできず――<br>娼館の一室に、再び嬌声が響き渡るのだった。": "Dù Yuri rơm rớm nước mắt nhưng chẳng thể cản nổi gã đàn ông――<br>Trong gian phòng kỹ viện, tiếng rên kiều mị lại tiếp tục vang vọng."
}

# ==============================================================================
# HMR_10220100023 (Yuri 2 Epilogue)
# ==============================================================================
translations["hmr_10220100023"] = {
    "うぅぅ～～……ま、まだ頭がふわふわしちゃいます……": "Ư... đ-đầu óc em vẫn còn lâng lâng...",
    "す、すみません……興奮してしまって、<br>ついつい夢中になって……な、何度も……": "X-Xin lỗi em... tôi hưng phấn quá nên không kiềm chế được...<br>l-làm nhiều lần quá...",
    "い、いえ……。それで満足して頂けたのであれば本望です。": "D-Dạ không sao... Chỉ cần anh thấy hài lòng là em vui rồi.",
    "それに、わたしを抱えてあんなに何度もできるのですものね。<br>きっと、足腰の筋力も、体力も申し分ないと思いますよ。": "Anh bế em làm được nhiều hiệp như thế,<br>thì thể lực đôi chân của anh thừa sức leo núi rồi.",
    "とはいえ、山では色んな危険が予想外に襲ってくるものです。<br>決して無理はせず、細心の注意を払って進んでくださいね。": "Tuy vậy trên núi luôn rình rập những nguy hiểm bất ngờ.<br>Anh tuyệt đối đừng gắng gượng quá sức và hãy cẩn thận nhé.",
    "……ふぅ。さすがに疲れました。<br>それにしても……": "...Phù. Mệt thật đấy.<br>Cơ mà...",
    "客を送り出し、ひとりになった部屋でユーリは鏡を見つめる。<br>そこには、さっきまで快楽に溺れていた名残を瞳に宿した、自分の姿があった。": "Sau khi tiễn khách, một mình trong phòng, Yuri ngắm mình trước gương.<br>Trong ánh mắt cô vẫn còn vương lại dư âm của sự đê mê khoái lạc.",
    "エッチしてる時のわたしって、あんな顔してるんだ……。<br>しれーとしてる時も、あんな感じなのかな……？": "Hóa ra lúc làm tình mặt mình lại như thế...<br>Lúc làm với anh Tư lệnh mình cũng có biểu cảm như vậy sao...?",
    "しれー……会いたいな……": "Anh Tư lệnh ơi... em nhớ anh quá...",
    "身体の芯に残る熱が、急激に寂しさへと形を変えていく。ユーリは確信する。<br>この胸の隙間を埋めることができるのは、世界でたった１人しかいない――": "Hơi ấm sâu trong cơ thể bỗng hóa thành nỗi cô đơn. Yuri tin chắc rằng,<br>người duy nhất có thể lấp đầy khoảng trống trong tim cô chỉ có một――"
}

# ==============================================================================
# HMR_10220100031 (Yuri 3 Intro)
# ==============================================================================
translations["hmr_10220100031"] = {
    "ある日の司令本部。山積みの報告書を前に、<br>死んだ魚のような目でペンを動かす<user>の姿があった。": "Một ngày nọ tại Bộ Tư lệnh. Trước đống báo cáo chất như núi,<br><user> đang cầm bút với ánh mắt vô hồn như cá chết.",
    "こんにちは……。あの……しれー、ちょっとお話したいことが……": "Em chào anh... Anh Tư lệnh ơi, em có chuyện muốn nói...",
    "深刻な表情を浮かべたユーリが訪ねてくる。<br>それを出迎えたのは、苦笑いを浮かべたアリシアだった。": "Yuri bước vào với nét mặt nghiêm túc.<br>Ra đón cô là Alicia với nụ cười gượng gạo.",
    "ああ、ユーリさん。司令官は今、大穴の報告書の処理に追われてまして。<br>ここ数日、ろくに眠れてないので……そろそろ限界ですね。": "A, cô Yuri. Tư lệnh đang bù đầu xử lý báo cáo về Hố Sâu.<br>Mấy ngày nay chưa được chợp mắt... anh ấy sắp kiệt sức rồi.",
    "机に向かい、青白い顔で虚ろな表情を浮かべている<br><user>の姿が、ユーリの目に入る。": "Yuri nhìn thấy <user> đang ngồi bên bàn làm việc<br>với gương mặt tái nhợt và ánh mắt thất thần.",
    "しれー、ボロボロじゃないですか……。<br>あ、あのアリシアさん！　ここのキッチンをお借りしてもいいでしょうか？": "Anh Tư lệnh tiều tụy quá rồi...<br>A-Alicia ơi! Em có thể mượn gian bếp ở đây được không ạ?",
    "キッチンですか？<br>それは構いませんけど……何かお料理でもされるんですか？": "Dùng bếp sao?<br>Được thôi, nhưng em định nấu món gì à?",
    "宿舎に、ノルトメキア神殿から取り寄せた特別な材料があるんです。<br>それを使って、しれーに栄養満点のお食事を作ってあげたいと思いまして！": "Ở ký túc xá em có nguyên liệu từ thần điện Nortmekia.<br>Em muốn dùng nó nấu món canh bổ dưỡng cho anh Tư lệnh!",
    "それはいいですねっ！　きっと司令官も喜びます！<br>キッチンはお好きに使ってください♪": "Ý hay đấy! Chắc chắn Tư lệnh sẽ vui lắm!<br>Em cứ tự nhiên dùng bếp nhé♪",
    "しばらくして、司令本部内には食欲をそそる芳醇な香りが漂い始める。<br>目の前に出された熱々のスープを、吸い込まれるように口へと運ぶ。": "Một lúc sau, mùi thơm ngào ngạt lan tỏa khắp phòng.<br>Tôi như bị cuốn hút mà húp từng thìa canh nóng hổi.",
    "う、美味い！　あんまり見たことのない食材ばかりだが、<br>これは美味すぎるぞ……っ！": "N-Ngon quá! Toàn nguyên liệu lạ mắt chưa từng thấy,<br>nhưng hương vị lại thơm ngon đến khó tin...!",
    "こちらは、わたしの住んでいたノルトメキアで採れる山菜や鶏肉、<br>それに香草をふんだんに使った滋養強壮スープです！": "Đây là món canh đại bổ nấu từ rau rừng, thịt gà<br>và rất nhiều thảo mộc đặc biệt của vùng Nortmekia đấy ạ!",
    "お仕事でお疲れの身体でもあっさり食べられて、栄養満点なんですよ。<br>すぐに元気になりますからね♪": "Món này thanh đạm dễ ăn lại cực kỳ bổ dưỡng.<br>Anh sẽ hồi phục sinh lực ngay thôi♪",
    "スープを口に運ぶ度、身体に異変が起き始める。それは単なる疲れが取れる<br>レベルではない。身体の芯から、熱い衝動がドクドクと突き上げてくるのだ。": "Mỗi thìa canh vào bụng, cơ thể tôi biến chuyển kỳ lạ.<br>Không chỉ tan mệt mỏi, mà một luồng nhiệt bỗng cuộn trào.",
    "しかし、完食する頃には、その”元気”は想定外の方向へと<br>暴走し始めていた。": "Thế nhưng khi ăn hết bát canh, 'sinh lực' dồi dào kia<br>lại bắt đầu bùng nổ theo một hướng hoàn toàn ngoài dự tính.",
    "こ、これは、確かに元気になってきたが……なんだか、身体が熱くて、<br>その、ある部位が特に……": "Đ-Đúng là anh thấy khỏe hẳn... nhưng người cứ nóng ran,<br>đặc biệt là... chỗ đó...",
    "ユーリの視線が下腹部を見つめる。身体が異様に熱く、ズボンの股間部分は、<br>こちらの意思に反してはっきりと形を変えてしまっているのだ。": "Yuri nhìn xuống hạ bộ của tôi. Toàn thân nóng bừng, đũng quần tôi<br>đã đội lên căng phồng trái với ý muốn.",
    "……しれー。……ずいぶん、効果が出てしまったみたいですね。<br>な、なんだか……下半身が苦しそうです……": "...Anh Tư lệnh. ...Xem ra tác dụng phát huy mạnh quá rồi.<br>T-Trông... phần dưới của anh có vẻ khó chịu lắm...",
    "あ、いや、これはだな……。<br>スープの栄養が、どうにも変な方向に流れて行ったみたいで……": "À không, chuyện này là...<br>Chất bổ trong bát canh dường như dồn hết về chỗ kỳ cục mất rồi...",
    "ユーリは恥ずかしさに耳まで赤くしながらも、<br>慈愛に満ちた瞳でこちらを見つめてくる。": "Yuri xấu hổ đỏ ửng cả vành tai,<br>nhưng vẫn nhìn tôi với ánh mắt đầy dịu dàng trìu mến.",
    "あの……しれーがよければ、ですけど……最後まで、<br>わたしに疲れた身体のお世話をさせてもらえませんか……？": "Ừm... nếu anh không phiền... thì hãy để em<br>chăm sóc cơ thể mệt mỏi của anh cho tới cùng nhé...?"
}

# ==============================================================================
# HMR_10220100032 (Yuri 3 H-scene)
# ==============================================================================
translations["hmr_10220100032"] = {
    "ベッドの上でユーリと向き合う。スープの熱が陽炎のように立ち上がり、<br>耐え難いほどの衝動が、こちらの理性を内側から削り取っていく。": "Đối diện Yuri trên giường, luồng nhiệt bốc lên như lửa đốt,<br>dục vọng mãnh liệt đang thiêu rụi lý trí tôi từ bên trong.",
    "さっきの食事なんなんだ？　身体が熱くて……歯止めが効かない……。<br>ユーリにそんな質問を投げかける。": "Món canh ban nãy là gì thế? Người anh nóng quá... không kìm được...<br>Tôi cất tiếng hỏi Yuri.",
    "アレは険しい山道を歩き続けるための滋養強壮スープですからね。<br>しれーの場合はその効果が下半身の方に集中しちゃったみたいですけど……": "Đó là canh bổ dưỡng để dẻo dai vượt đường núi mà.<br>Với anh Tư lệnh thì tác dụng dồn hết xuống phần dưới...",
    "でも……大丈夫です。<br>わたしは、その……受け止める覚悟はできてますから……": "Nhưng... không sao đâu ạ.<br>Em... đã chuẩn bị tinh thần để đón nhận tất cả rồi...",
    "ユーリが揺れる瞳でこちらを見つめる。<br>抑えられない欲情のまま、ユーリに襲い掛かってしまう。": "Yuri nhìn tôi với ánh mắt run rẩy ướt át.<br>Trước cơn dục vọng không thể kìm nén, tôi lao tới ôm lấy cô bé.",
    "はぁぁぁ～～～……んんっ……ぁああぁぁ～～～ッ！！": "Haaaa... ưm... aaaaa...!!",
    "挿入の衝撃、そして待ちわびた熱に当てられ、<br>ユーリは顎を跳ね上げる。": "Trước cú đâm mạnh mẽ và hơi nóng hằng mong đợi,<br>Yuri ngửa cổ ra sau rên rỉ.",
    "はぁっ……はぁっ……はぁっ……<br>い、イっちゃった……": "Hà... hà... hà...<br>E-Em ra mất rồi...",
    "どうやら、挿入しただけで軽く絶頂したらしい。<br>……まさか、もうイったのか？　そう訊く。": "Có vẻ chỉ vừa mới đút vào cô bé đã đạt cực khoái nhẹ.<br>...Không lẽ em vừa lên đỉnh rồi sao? Tôi hỏi.",
    "は、はい……だ、だって楽しみにしていたから……あっ！<br>あぁぁっ！　あっ、はぁぁっ！": "V-Vâng... t-tại em mong chờ quá mà... a!<br>Aaa! A, haaa!",
    "急に始まった抽送に、たまらずユーリは甲高い嬌声を上げる。<br>前回の遭難時よりも硬く膨れ上がった肉棒が、膣内を容赦なく蹂躙していく。": "Trước những cú nhấp dồn dập, Yuri cất tiếng rên kiều mị.<br>Thanh thịt cương to hơn cả lần trước không tiếc cày xới bên trong.",
    "あっ！　あぁっ、はぁぁんっ……！": "A! A, haaa...!",
    "（ぁあっ……しれーのオチンチン……硬くて……<br>こないだよりも……す、凄く熱い！！）": "(A... dương vật của anh ấy... cứng quá...<br>còn nóng hơn cả hôm trước nữa...!)",
    "その時、彼女の熱心すぎる反応と、<br>スープの過剰な効果にある１つの疑念を抱いてしまう。": "Lúc này, trước phản ứng của cô và công hiệu của món canh,<br>tôi bỗng nảy sinh một mối nghi ngờ.",
    "そのことが、急に冷静さを呼び戻し、<br>次第に腰の動きを止めてしまう。": "Nghi vấn ấy làm tôi chợt tỉnh táo lại,<br>từ từ dừng nhịp chuyển động của hông.",
    "えっ？　あ、あの……ど、どうかしたんですか？ <br>……しれー……？　も、もうっ！　焦らさないでくださいよ……": "Eh? Ơ... a-anh sao thế ạ?<br>...Anh ơi...? Thật là! Đừng làm em sốt ruột mà...",
    "不満げに、けれど切なそうに訴えてくるユーリ。<br>その瞳をじっと見つめて、浮かんだ疑問を問いかける。": "Yuri phụng phịu trách móc nhưng ánh mắt đầy khát khao.<br>Tôi nhìn thẳng vào mắt cô bé và hỏi câu hỏi trong lòng.",
    "ひょっとして、こうなるのを望んでわざとあの料理を作ったのではないか？": "Có phải em cố tình nấu món đó vì muốn chuyện này xảy ra đúng không?",
    "そ、それは……っ！": "C-Chuyện đó là...!",
    "図星を突かれ、しどろもどろになるユーリ。<br>その瞳は明らかに動揺で泳いでしまっている。": "Bị nói trúng tim đen, Yuri ấp úng bối rối.<br>Ánh mắt cô bé đảo lia lịa vì ngượng ngùng.",
    "お前は神に仕える身のはずなのにいいのか？　こんな罪なことして――<br>と、呆れたように告げる。": "Em là người phụng sự thần linh cơ mà? Làm thế này có sao không đấy――<br>tôi vờ thở dài trêu cô.",
    "いいえ、これは罪なことではありません！ <br>だ、だって……今わたしは、しれーに仕える身ですから！": "Không, đây đâu phải tội lỗi!<br>V-Vì... bây giờ em là người phụng sự anh Tư lệnh mà!",
    "彼女は真っ直ぐに、力強く宣言した。神への忠誠よりも、<br>今、目の前にいる自分への献身を選ぶと言うのだ。": "Cô bé dõng dạc tuyên bố. Rằng thay vì trung thành với thần linh,<br>cô chọn dâng hiến trọn vẹn cho người đang ở trước mắt.",
    "ですから……続けては、くれませんか……？": "Vì vậy... anh tiếp tục làm tiếp được không ạ...?",
    "ユーリのあまりに真剣な表情での訴えに、思わず吹き出してしまう。<br>分かったよ、お前の望むようにしてやる――そう苦笑して告げる。": "Thấy Yuri nghiêm túc cầu xin đến mức đáng yêu, tôi phì cười.<br>Được rồi, anh sẽ chiều theo ý em―― tôi cười đáp.",
    "ぅんっ！　ぁああっ……はぁっ……ぅうんっ！<br>あぁっ……や、やっぱり気持ち……いぃ！": "Ưm! Aaa... hà... ưm!<br>A... quả nhiên sướng... quá đi mất!",
    "抽送を再開すると、ユーリが再び甘い嬌声をあげ始める。<br>肉と肉がぶつかり合う音が部屋に響いていく。": "Khi tôi tiếp tục nhấp hông, Yuri lại cất tiếng rên ngọt ngào.<br>Tiếng da thịt va chạm bì bạch vang vọng khắp căn phòng.",
    "はぅんっ！　ぁああっ、はぁっ、ぅうんっ！<br>し、しれー……はぁぁぁっ！　も、もっと気持ち良くして……": "Haaa! Aaa, hà, ưm!<br>A-Anh ơi... haaa! Hãy làm cho em sướng hơn nữa đi...",
    "んぅっ……ひあっ！？　あっ、あっ……！　しれーのが、気持ち、<br>良すぎてぇ……んぅっ！　おなか、キュンキュンしちゃいますぅ……！": "Ưm... hya!? A, a...! Của anh sướng quá đi mất...<br>ưm! Bụng dưới của em cứ thắt lại từng cơn rồi...!",
    "いつにも増した甘いユーリの声に、昂ぶっていく。<br>もっともっと、この少女を乱れさせたくなる。": "Giọng rên nũng nịu của Yuri khiến tôi càng thêm hưng phấn.<br>Tôi muốn làm cho cô bé này đê mê hơn nữa.",
    "はぅっ……！？　んくっ、ふあっ、あっ、ぁっ、あぁぁっ……！": "Hức...!? Ưm, phù, a, a, aaaa...!",
    "腰の向きを変え、ユーリの膣壁を様々な角度で突く。<br>単純な抽送に慣れつつあったユーリに新鮮な刺激を与えていく。": "Tôi đổi góc hông, thúc vào thành âm đạo của Yuri từ nhiều hướng,<br>mang lại những kích thích mới lạ cho cô bé.",
    "あぁっ！　はぁっ、うっ……！　こ、これっ……すごいですっっ！<br>オチンチンがぁ、わたしの、いろんなところに当たってぇぇ……はぁんっ♡": "A! Hà, ư...! C-Cái này... tuyệt quá...!\nDương vật của anh chạm vào khắp mọi nơi trong em... haaa♡",
    "角度を変えて腰を突き入れるたび、ユーリはおもしろいくらい敏感に反応する。<br>艶めかしく身体をよがらせるユーリの姿に、こちらの息も荒くなる。": "Mỗi lần đổi góc thúc, Yuri đều phản ứng nhạy cảm mê người.<br>Thấy cô uốn éo thân mình đầy dâm mỹ, hơi thở tôi cũng dồn dập theo.",
    "ユーリの膣はびくびくと痙攣するように蠕動し、こちらの肉棒を<br>きゅっと締め上げてくる。膣襞がカリ首をこそぎあげ、思わず声が漏れる。": "Âm đạo Yuri co thắt giật giật, siết chặt lấy thanh thịt của tôi.<br>Nếp gấp niêm mạc miết chặt lấy quy đầu làm tôi bật tiếng rên.",
    "ああぁっ、気持ち、……いいっ！　し、しれー……！<br>も、もっともっと……激しくしてくださぁい……っ！": "Aaa, sướng... quá! A-Anh ơi...!\nX-Xin anh hãy làm mạnh hơn... mạnh hơn nữa đi ạ...!",
    "どこまでも貪欲にこちらを求めてくるユーリに、自制がきかなくなっていく。<br>寝不足のはずなのに体力は尽きることなく、突き出す腰にさらに力がこもる。": "Sự khao khát vô tận của Yuri khiến tôi mất hết kiềm chế.<br>Dù thiếu ngủ nhưng sinh lực vẫn dồi dào, tôi thúc càng mạnh hơn.",
    "あぁっ……い、いいですぅっ！　ぁああぁっ、あぁっ……！<br>わたしの気持ちいいところに、ズンズンって当たってぇ……はああぁぁっ！": "A... t-tuyệt quá! Aaa, a...!\nĐâm trúng vào chỗ sướng nhất của em rồi... haaa!",
    "腰を大きく引き、そのぶん深く突く。<br>ストロークは長く、けれど抽送はさらに速く、ユーリの蜜壷を激しくかき回す。": "Tôi rút hông ra thật xa rồi thúc thật sâu vào trong.<br>Biên độ dài và nhịp thúc nhanh khuấy đảo hoa huyệt của Yuri.",
    "あっ、ふあっ、ひうっっ……！　そこっ……んんっ……いぃっ！<br>あはぁ……っ、もうっ、気持ち良すぎて……っ、だめぇぇ……♡": "A, phù, hức...! Chỗ đó... ưm... sướng quá!\nA... sướng quá mức rồi... không chịu nổi nữa đâu...♡",
    "極限の快楽に、ユーリは髪を振り乱して翻弄されている。<br>小さな身体には激しすぎるかとも思ったが、こちらを求める声はやまない。": "Trong cơn cực khoái, Yuri lắc lư mái tóc đắm chìm vào nhục cảm.<br>Dù sợ cơ thể nhỏ nhắn quá tải, tiếng cô cầu xin vẫn không ngừng vang lên.",
    "あっ、あっ……また、きてるっ……！　し、しれー……わた、し……っ。<br>また、イっちゃいそう、ですぅ……はっあぁん！": "A, a... lại tới nữa rồi...! A-Anh ơi... em...<br>Em lại sắp ra nữa rồi... a haaa!",
    "ビクビクと膣壁が震える。まるで精液を搾り取ろうと蠕動しているようだ。<br>こちらももう、限界が近かった。": "Thành âm đạo giật thắt liên hồi như muốn vắt kiệt tinh dịch.<br>Bản thân tôi cũng đã tiến rất gần tới bờ vực giải tỏa.",
    "お、お願い……今度イク時は、しれーと一緒がいいですっ！ <br>だ、だから……！": "X-Xin anh... lần này lên đỉnh em muốn ra cùng lúc với anh!<br>V-Vì thế...!",
    "ユーリの身体をつかむ手に力を込め、スパートをかける。<br>子宮を突き上げるような激しい抽送に、ユーリの嬌声があがる。": "Tôi siết chặt người Yuri và bắt đầu tăng tốc hết mức.<br>Những cú thúc sâu chạm tử cung làm vang lên tiếng rên kiều mị.",
    "はっ、あっ、ふっ、ひあ……っ！　イ、イキます……、<br>わたし、イっちゃいますぅ～～！　しれーも、一緒にぃ～……！": "Hà, a, hức... e-em ra đây...<br>em lên đỉnh đâyyy! Anh cũng ra cùng em nhé...!",
    "腰の奥が大きく震える。膨れ上がった灼熱の濁流が、<br>決壊したように陰茎へと流れ込む。そして――": "Sâu trong thắt lưng rung lên dữ dội. Dòng tinh dịch nóng bỏng<br>như vỡ đê dồn hết về đầu dương vật. Và rồi――",
    "い、イクっ！　ぁあっはぁぁっ……んんっはあぁぁぁ～～～ッ！！！！": "E-Em ra đâyyy! Aaaa... ưm haaaaa...!!!!",
    "ユーリは背中を仰け反るようにして絶頂に達する。と、ほぼ同時に<br>亀頭が爆発し、大量の白濁液がユーリの子宮目掛けて放出されていく。": "Yuri ưỡn cong lưng đón nhận cực khoái. Gần như cùng lúc,<br>quy đầu bùng nổ, bắn lượng lớn tinh dịch xối thẳng vào tử cung.",
    "はぁっ……はぁっ……んんっ……。ぁっ……はぁっ……。<br>しれーの精液……あったかくって……気持ち……いぃ……": "Hà... hà... ưm... a... hà...<br>Tinh dịch của anh... ấm áp quá... sướng... lắm...",
    "満足感に包まれ、しばし呆然としていたユーリ。<br>しかし、彼女の仕掛けた滋養強壮スープの効果は、まだ終わってはいなかった。": "Đắm chìm trong mãn nguyện, Yuri nằm ngẩn ngơ một lúc.<br>Thế nhưng công hiệu của món canh tráng dương vẫn chưa dừng lại.",
    "あ……しれーの、また大きくなってきましたね……": "A... của anh lại to lên nữa rồi kìa...",
    "射精直後にも関わらず、再び脈打ち始めた肉棒の脈動を感じ、<br>ユーリは愛おしそうに微笑む。": "Dù vừa xuất tinh, cảm nhận được thanh thịt đang đập rộn ràng,<br>Yuri mỉm cười đầy âu yếm.",
    "ん……んん……っ！　んっ……はぁぁっ……！": "Ưm... ưm...! Ưm... haaa...!",
    "彼女は自らゆっくりと腰を動かし始め、<br>その熱を再び内側へと迎え入れようとする。": "Cô bé bắt đầu chậm rãi tự đưa hông,<br>đón nhận lại luồng nhiệt ấy vào sâu bên trong mình.",
    "んっ……はぁぁっ……！　わたしは大丈夫ですよ……？<br>気が済むまで、何回でもおかわりしてくださっていいですから……": "Ưm... haaa...! Em không sao đâu ạ...<br>Bao nhiêu hiệp cũng được, anh cứ làm tới khi thỏa mãn nhé..."
}

# ==============================================================================
# HMR_10220100033 (Yuri 3 Epilogue)
# ==============================================================================
translations["hmr_10220100033"] = {
    "窓の外から差し込む柔らかな朝の光が、寝室を白く染めていた。<br>昨夜の激しい情事の名残が嘘のように、穏やかで清々しい空気が流れている。": "Ánh bình minh dịu nhẹ rọi qua cửa sổ, nhuộm trắng phòng ngủ.<br>Bầu không khí trong lành xua tan đi dấu vết cuồng nhiệt đêm qua.",
    "目が覚めた<user>の隣では、すでに身なりを整えた<br>ユーリが、聖母のような優しい微笑みを浮かべて待っていた。": "Bên cạnh <user> vừa thức giấc, Yuri đã chỉnh tề trang phục<br>đang mỉm cười dịu dàng như một vị thánh mẫu.",
    "おはようございます、しれー。<br>ぐっすり眠れましたか？": "Chào buổi sáng anh Tư lệnh.<br>Anh ngủ có ngon giấc không ạ?",
    "あぁ……。結局、昨夜は何回したのか途中から記憶がないが、<br>おかげでぐっすり寝られたよ。": "Ừ... Rốt cuộc tối qua làm bao nhiêu hiệp anh chẳng nhớ nổi,<br>nhưng nhờ vậy mà ngủ một giấc thật say.",
    "身体を起こすと、不思議な感覚が<user>を包む。<br>連日の疲労が抜け、身体がスッキリと軽く、内側から活力が漲ってくるのだ。": "Khi ngồi dậy, một cảm giác kỳ diệu bao bọc lấy <user>.<br>Bao mệt mỏi tan biến, người nhẹ nhõm và sinh lực tràn trề.",
    "あの料理のおかげか……身体がメチャメチャ軽く感じる……。<br>す、すごい効果だな。": "Nhờ món canh đó sao... Người anh nhẹ bẫng đi này...<br>T-Tác dụng thần kỳ thật đấy.",
    "はい。山の神は、人に生きる力を与えてくれる神ですから！<br>よく食べ、生きる力を蓄えるのもその教えの１つなのです。": "Vâng ạ. Thần núi là vị thần ban sinh mệnh cho con người mà!<br>Ăn uống đủ chất để tích lũy sinh lực cũng là một giáo lý đó.",
    "なるほど、生きる力ね……。<br>それにしても昨晩は、自分でも驚くほどの精力だった気がするよ。": "Ra là vậy, sinh lực sống à...<br>Cơ mà đêm qua sinh lực dồi dào đến mức chính anh cũng giật mình.",
    "仕事でお疲れの時は、いつでも呼んでくださいね。<br>また、滋養強壮料理を振る舞ってさしあげますから。": "Khi nào mệt mỏi vì công việc, anh cứ gọi em bất cứ lúc nào nhé.<br>Em sẽ lại nấu món ăn tẩm bổ cho anh.",
    "それはありがたいが……あれを食べると、下半身のほうまで<br>元気がありあまってしまうからなぁ……": "Được thế thì quý quá... nhưng hễ ăn món đó là phần dưới<br>lại sung mãn quá mức cho xem...",
    "安心してください。その時はもちろん――<br>そちらのお世話もさせていただきますから……": "Anh yên tâm đi ạ. Những lúc ấy đương nhiên――<br>em cũng sẽ chăm sóc luôn phần đó cho anh...",
    "一点の曇りもない、ひまわりのような明るい笑顔。<br>それが彼女にとって、神に仕えることと同義の、至極真っ当な愛の形なのだ。": "Nụ cười rạng rỡ như hoa hướng dương không gợn chút ưu phiền.<br>Với cô, đó là cách thể hiện tình yêu thiêng liêng như khi phụng sự thần.",
    "<user>は降参したように肩をすくめ、<br>自分に向けられたその献身を、改めて愛おしく抱きしめるのだった――": "<user> nhún vai chịu thua,<br>rồi ôm chầm lấy cô bé đầy âu yếm đón nhận sự tận tụy ấy――"
}

# ==============================================================================
# HMR_11030100011 (Naia 1 Intro)
# ==============================================================================
translations["hmr_11030100011"] = {
    "深夜――遅くまで仕事を頑張っていた<user>に、<br>ナイアが料理を振舞っていた。": "Đêm khuya―― Naia bưng những món ăn nóng hổi<br>đến chiêu đãi <user> đang vất vả làm việc muộn.",
    "ねぇねぇ、どうだった？　<br>ナイアシェフの元気どっかんフィーバーハンバーグっ！": "Này này, anh thấy sao hả?<br>Món thịt băm viên bùng nổ năng lượng của bếp trưởng Naia đấy!",
    "ああ、味付けも完璧で、ボリュームもたっぷりだった。<br>美味かったよ、いやぁ、流石はナイアシェフだ。": "Ừ, nêm nếm hoàn hảo mà khẩu phần lại đầy ắp.<br>Ngon lắm, quả không hổ danh bếp trưởng Naia.",
    "でしょでしょ～！<br>えへへっ、やったぁっ♪": "Đúng không nào~! Em biết ngay mà!<br>Hi hi, tuyệt quá đi♪",
    "（間違いなく美味いんだが、<br>料理名だけはアレなんだよな……）": "(Ngon thì ngon thật đấy,<br>nhưng cái tên món ăn thì đúng là ba chấm...)",
    "また料理、持ってくるからね！<br>期待しててよっ♪": "Lần sau em sẽ lại nấu mang qua nhé!<br>Hãy đón chờ đấy nhé♪",
    "あぁ、ありがとな。<br>食器、運ぶの手伝おうか？": "Ừ, cảm ơn em nhé.<br>Để anh giúp em bê bát đĩa một tay?",
    "ううんっ、大丈夫。お料理上手は片付け上手っ。<br>ひとり分のお皿くらい、へっちゃらだから♪": "Dạ không cần đâu. Nấu giỏi thì dọn dẹp cũng giỏi mà.<br>Chút bát đĩa của một người em lo loáng cái là xong♪",
    "そうか……ならドアくらいは開けさせてくれ。<br>――ん？　あれ、変だな……？": "Vậy sao... thế để anh mở cửa giúp em.<br>――Hm? Ơ, lạ thật đấy...?",
    "どうしたの？<br>もしかしてドアノブ、動かない？": "Sao thế anh?<br>Không lẽ tay nắm cửa bị kẹt rồi sao?",
    "……そ、そうらしい。壊れたみたいだ。<br>参ったな、ドアが開かないぞ。": "...C-Có vẻ là vậy. Hỏng mất rồi.<br>Gay go thật, cửa không mở được nữa.",
    "えぇ～！？<br>もしかして、こんなところでも私の不幸体質が発動しちゃったのぉ！？": "Eh~!?<br>Không lẽ ở đây mà vận xui của em cũng phát huy tác dụng sao!?",
    "時間が時間だから、蹴破って外に出るのも良くないな。<br>みんなを起こしてしまう。": "Đêm hôm thế này đạp cửa ra ngoài cũng không hay.<br>Sẽ làm phiền đánh thức mọi người dậy mất.",
    "朝になったら誰か来るはずだ、助けてはもらえるだろう。<br>それまで、一緒に過ごすか……": "Đến sáng chắc sẽ có người tới giải cứu thôi.<br>Từ giờ đến lúc đó, đành ở chung với nhau vậy...",
    "つまり……今夜は、司令官さんとふたりきり……って、こと……？": "Tức là... đêm nay, chỉ có hai chúng ta ở riêng với nhau sao...?",
    "安心してくれ。俺は床で寝る。<br>ナイアはベッドを使ってくれ。": "Em yên tâm đi. Anh sẽ ngủ dưới sàn.<br>Naia cứ dùng giường nhé.",
    "わ、私が床でいいよっ。<br>私、落とし穴の中で一晩明かしたことだってあるんだからっ！": "E-Em ngủ sàn được mà!<br>Em từng ngủ qua đêm trong hố bẫy rồi nên không sao đâu!",
    "そりゃまた災難だったな……。<br>だが、俺はナイアに無理をさせたくない、遠慮なくベッドを使ってくれ。": "Thế thì xui xẻo thật đấy...<br>Nhưng anh không muốn em chịu khổ, cứ tự nhiên nằm giường đi.",
    "む、無理をさせたくないのは、私も一緒だよ～。": "E-Em cũng không muốn anh phải chịu khổ đâu mà~.",
    "それか、その……ふたりとも同じ気持ちなら……<br>一緒に、寝る？": "Hay là... nếu cả hai đều nghĩ như thế...<br>thì ta ngủ chung nhé?",
    "……俺は構わないが、間違いが起こるかもしれないぞ？": "...Anh thì không ngại, nhưng có khi xảy ra chuyện ngoài ý muốn đấy?",
    "いいよ、私は……司令官さんとなら……": "Em không sao đâu... nếu là với anh Tư lệnh...",
    "――もう言葉はいらなかった。<br>ふたりは手を繋いで、ベッドへ歩いていく。": "――Chẳng cần thêm lời nào nữa.<br>Cả hai nắm lấy tay nhau và cùng bước về phía giường."
}

# ==============================================================================
# HMR_11030100012 (Naia 1 H-scene)
# ==============================================================================
translations["hmr_11030100012"] = {
    "ナイアの服をずらし、隠されていた部分をあらわにする。<br>整った胸は寝転がっていても形が崩れず、乳首をツンと天井へ立たせていた。": "Tôi vén áo Naia lên, để lộ cơ thể ngọc ngà giấu kín.<br>Đôi gò bồng đảo căng tròn dựng đứng hai đầu nhũ hoa kiêu hãnh.",
    "うぅぅ……あまり見ないでぇ……恥ずかしいからぁ……": "Ư... đừng nhìn chằm chằm thế mà... ngượng lắm...",
    "頬を赤らめ、弱々しい声で訴えかけてくるナイア。<br>初めてなのか？　と、刺激を与えないように静かな声で尋ねてみた。": "Naia đỏ bừng má, khẽ thì thầm cầu xin.<br>Lần đầu của em à? Tôi hạ giọng dịu dàng hỏi để em bớt căng thẳng.",
    "あ、あたりまえだよ……<br>男の人におっぱいも、大事なところも、見せたことなんてないもん……": "Đ-Đương nhiên rồi ạ...<br>Em chưa từng cho người đàn ông nào thấy ngực hay chỗ quan trọng cả...",
    "耳まで真っ赤に染め上げているのでどうにもからかいたくなる。<br>フェルトゥーナという娘がいるじゃないか――と軽口を叩いてしまった。": "Thấy tai em đỏ rực, tôi không nhịn được trêu chọc.<br>Chẳng phải em có đứa con gái tên Fortuna sao―― tôi buột miệng đùa.",
    "も、もぉ～っ。<br>からかわないでよぉ～……": "Th-Thật là~.<br>Đừng có trêu em nữa mà~...",
    "すまん、と素直に謝る。初めてなのだから、優しくしないと――<br>軽口ではなく、快楽で緊張を解こうと心に決め、ナイアに触れていく。": "Anh xin lỗi, tôi chân thành nhận lỗi. Lần đầu thì phải nhẹ nhàng――<br>Tôi quyết định dùng khoái lạc xoa dịu nỗi sợ và chạm vào Naia.",
    "んあぁ……はぁっ……はうっ……": "Ưm a... hà... hức...",
    "隆起した男性器の裏筋をクリトリスに擦り付け、快感を丁寧に送り込む。<br>愛撫を受けた彼女は小さく吐息して、いじらしく反応した。": "Tôi dùng phần gân dương vật cọ lên hột le, tỉ mỉ truyền khoái cảm.<br>Được vuốt ve âu yếm, em khẽ thở dốc và phản ứng đầy đáng yêu.",
    "あ、熱い……。<br>これがおちんちん……んっ、んぅぅ……": "A, nóng quá...<br>Đây là dương vật sao... ưm, ư...",
    "ひくひくひくっ、とクリトリスが喘いでいるのが分かる。<br>――感じやすい体質のようだ、と教えるように告げた。": "Có thể cảm nhận được hột le đang giật giật từng nhịp.<br>――Em nhạy cảm thật đấy, tôi khẽ thì thầm bên tai em.",
    "ふぅ、ん……い、言わないでぇ……<br>恥ずかしすぎて身がもたないよぉ～……っ。": "Phù, ưm... đ-đừng nói ra mà...<br>Xấu hổ chết mất thôi anh ơi~...",
    "（だ、だめぇ……初めてなのに、気持ちいい……）": "(K-Không được rồi... lần đầu mà sao sướng thế này...)",
    "（……あれ？　司令官さんのおちんちんも硬くなってるような……？<br>ひょっとして――私で興奮してくれてるの、かな……？）": "(...Ủa? Dương vật của anh Tư lệnh cũng cứng ngắc lên rồi kìa...?\nChẳng lẽ―― anh ấy vì mình mà hưng phấn sao...?)",
    "悶えるナイアを見ていると、こちらも昂ってきた。<br>――挿れるぞ？　と問い掛ける。": "Nhìn Naia quằn quại, dục vọng trong tôi cũng sôi sục.<br>――Anh đút vào nhé? Tôi cất tiếng hỏi.",
    "（は、恥ずかしい……けど、司令官さんなら――<br>司令官さんも、興奮してくれてるなら……）": "(X-Xấu hổ quá... nhưng nếu là anh Tư lệnh――\nNếu anh ấy cũng muốn mình đến thế...)",
    "はい……私の初めて、もらってください……": "Vâng... xin hãy nhận lấy lần đầu tiên của em...",
    "しおらしく返事をする彼女に、愛おしさが込み上げてくる。<br>ぐっと硬さを増した怒張の先端で入り口をこじ開けにいく――": "Nghe câu trả lời e ấp, lòng tôi trào dâng niềm yêu thương.<br>Tôi dùng quy đầu căng cứng tách mở lối vào chật hẹp――",
    "んぁっ……はあ、ああぁっ……あああああんっ！": "Ưm a... ha, aaaa... aaaaa!",
    "気遣いながら、最奥へと押し入れた。<br>目尻に涙が溜まっているが、ナイアは必死に耐えてくれている。": "Tôi nhẹ nhàng đẩy thẳng vào nơi sâu nhất.<br>Khóe mắt rưng rưng ngấn lệ, nhưng Naia vẫn cắn răng chịu đựng.",
    "はぁふ……んぅぅ～……ぜ、全部、入ったぁ？": "Hà... ưm~... v-vào hết bên trong rồi sao anh?",
    "よく頑張ったなと声をかけた。<br>一方ナイアは繋がった部分を興味深そうに注視している。": "Em giỏi lắm, tôi dịu dàng khen ngợi.<br>Còn Naia thì tò mò chăm chú nhìn nơi hai cơ thể gắn kết.",
    "すごい……私のおまんこが、おちんちん食べちゃってるみたい……。<br>んっ……すごく硬いよ……勝手に締まっちゃう……": "Tuyệt quá... hoa huyệt của em như nuốt trọn lấy dương vật vậy...<br>Ưm... cứng quá... nó cứ tự động siết chặt lại...",
    "その言葉通り、膣内はギチギチに容赦なく肉棒を咀嚼してくる。<br>だが拒絶するのではなく、余すところなく快感を味わおうとする動きだった。": "Đúng như em nói, âm đạo siết chặt lấy thanh thịt không kẽ hở.<br>Nhưng đó không phải cự tuyệt, mà là muốn mút trọn khoái cảm.",
    "膣内はまさに蜜壺と言えるほどに濡れそぼっている。<br>じっとしているのが耐え難いほどに心地がよく、思わず陰茎に力がこもる。": "Bên trong ướt đẫm như một mật động ngọt ngào.<br>Cảm giác êm ái khiến tôi không thể đứng yên, bất giác gồng cứng.",
    "（あ……司令官さんのおちんちん、ヒクヒクしてる……<br>これって動きたい……のかな？）": "(A... dương vật của anh Tư lệnh đang giật giật kìa...<br>Có phải anh ấy muốn chuyển động rồi không...?)",
    "ふぅ、はぁ……私は大丈夫だから……ん……いいよ、動いて……？": "Phù, hà... em không sao đâu... ưm... anh cứ nhấp đi...?",
    "この上なく、魅力的な提案だった。<br>そのまま膣内の収縮にも背中を押される形で、肉棒を動かし始める――": "Một lời mời gọi không gì quyến rũ hơn.<br>Được sự co bóp bên trong thúc giục, tôi bắt đầu đưa đẩy thanh thịt――",
    "んあぁっ……あっ、ふぅ――はぁぁ……っ。": "Ưm a... a, phù―― haaa...",
    "ゆさっ、ゆさっ、とベッドの上でナイアと一緒に身体を揺らす。<br>手前から奥へ進むたび、奥から引き抜くたび、彼女は可愛らしく喘いだ。": "Cả hai cùng rung lắc nhịp nhàng trên giường.<br>Mỗi nhịp rút ra thúc vào sâu, em lại cất tiếng thở dốc đáng yêu.",
    "あっ、やだっ……どうしてこんなにぃ……あっ、んあっ……": "A, không muốn đâu... sao lại sướng thế này... a, ưm...",
    "くちゅくちゅ――と粘り気のある淫靡な音が混じり始める。<br>割れ目から愛液が零れて飛び散っているに違いない。": "Tiếng lép bép nhóp nhép dâm mỹ bắt đầu vang lên.<br>Dâm dịch từ nơi giao hợp đang trào ra ướt đẫm.",
    "もちろんこちらも腰が震えるほどの快楽を覚えていた。<br>敏感な亀頭で蜜襞をゾリゾリと擦り上げる感触がたまらない。": "Bản thân tôi cũng run rẩy vì sướng ngất ngây.<br>Cảm giác quy đầu miết qua từng nếp gấp âm đạo thật đê mê.",
    "やぁっ、はんっ……あああっ……だめぇっ……。<br>はじめて、なのに……声が漏れちゃう……恥ずかしいよ……": "A, ha... aaa... không được đâu...<br>Lần đầu tiên mà... tiếng rên cứ tuôn ra... xấu hổ quá...",
    "恥ずかしがる必要はない。もっと聴かせてほしい――<br>男は好きな人の甘い声が好きなんだと、素直に告げてみる。": "Không cần xấu hổ đâu, anh muốn nghe nhiều hơn nữa――<br>Đàn ông luôn thích nghe tiếng rên ngọt ngào của người mình yêu mà.",
    "んへぇ？　私のことが、好き……？　司令官さんが……？<br>でもでも、私、ドジだし……運が悪いし……あ、あぁん……": "Hả? Anh thích em sao...? Anh Tư lệnh á...?<br>Nhưng mà em hậu đậu... lại hay gặp xui xẻo nữa... a, a...",
    "そんなところが好きだ。不幸に負けずにがんばるところが<br>ナイアらしくて大好きだ――その言葉と共に、腰を強く打ち付けていく。": "Anh thích chính những điều đó. Luôn kiên cường vượt qua xui xẻo<br>mới đúng là Naia anh yêu―― tôi vừa nói vừa thúc mạnh hông vào.",
    "ふあああっ！？　あ、あぁあっ！<br>あああっ、し、司令官さんっ……！　あっ、あっ、あっ……！": "Oa a!? A, aaaa!<br>Aaa, a-anh Tư lệnh...! A, a, a...!",
    "ばちゅ、ばちゅ、と水が弾ける音が部屋に響く。<br>ナイアは小さな身体で、猛々しい動きをしっかり受け止めていた。": "Tiếng da thịt bì bạch lẫn tiếng nước vang dội trong phòng.<br>Thân hình nhỏ nhắn của Naia đón nhận trọn vẹn từng cú đâm dũng mãnh.",
    "甲高い声を上げながら、ナイアは絡めている指をギュッと握り込んでくる。<br>滲んでいる手汗の量が彼女の興奮を物語っていた。": "Vừa cất tiếng rên cao vút, Naia vừa đan chặt mười đầu ngón tay.<br>Mồ hôi ướt đẫm lòng bàn tay chứng tỏ em đang hưng phấn tột độ.",
    "ふあっ、あああっ……そ、そんなに――私のこと、好きなの……ッ？": "Phù, aaa... a-anh thích em―― đến thế sao...?",
    "――じゃないと、こんなに求めたりしない。<br>膨らみと硬さが一段と増した肉棒で、膣内を責め立てる。": "――Không thích thì anh đâu có khao khát em đến mức này.<br>Tôi dùng thanh thịt trướng to cương cứng khuấy đảo bên trong em.",
    "あぁぁうぅ……！　すごいっ……あ、あっ……あっ……！！<br>嬉しい……司令官さんに求めてもらえて……幸せぇ……っ！": "Aaa ư... tuyệt quá... a, a... a...!!<br>Em vui lắm... được anh khao khát... em hạnh phúc quá...!",
    "蕩けるような声に、抑え切れない愛情と情欲が灯る。<br>そして彼女の眼差しからもより熱を感じるようになった。": "Trong giọng rên mê đắm ánh lên tình yêu và dục vọng cháy bỏng.<br>Ánh mắt em nhìn tôi cũng ngày một nồng nàn hơn.",
    "んああぅぅっ！<br>私も、司令官さんのこと――すきぃ……っ！": "Ưm aaa!<br>Em cũng... yêu anh Tư lệnh nhiều lắm...!",
    "あ、あ、ああぁぁ……！　や、やだ、どうしよう！<br>また勝手にナカ、締まっちゃ……んん～～っ♡": "A, a, aaaa...! Đ-Đừng mà, làm sao đây!<br>Bên trong lại tự siết chặt lấy... ưm~~♡",
    "好きという言葉が漏れた瞬間、狭かった膣内がいっそう強烈に締まった。<br>根本から先端まで隙間なく張り付いた膣壁が収縮――グイグイと絞られる。": "Khoảnh khắc lời yêu thốt ra, bên trong càng thắt chặt dữ dội hơn.<br>Thành âm đạo mút chặt từ gốc tới ngọn―― bóp nghẹt lấy thanh thịt.",
    "はっ、あ、あうっ、んんぅ……すき、すきぃ……！<br>ひあっ……すき、すきなのぉ……！": "Hà, a, ư... yêu anh, em yêu anh lắm...!\nHya... em yêu anh nhiều lắm...!",
    "言われるたび、やはり膣内が収縮を繰り返す。<br>その動きからも情愛が感じられた。こちらも、その想いに応えたい――": "Mỗi lời em nói, bên trong lại co bóp từng hồi chứa chan tình cảm.<br>Tôi cũng muốn đáp lại trọn vẹn tình cảm nồng nàn ấy――",
    "ああああっ！　子宮に当たってぇ……！？<br>ふぁぁ！　あああ、ああああっ！": "Aaaa! Đâm trúng tử cung rồi...!?<br>Oa! Aaa, aaaa!",
    "最奥を突く瞬間、さっきよりも先端をねじ込むような意識で腰を進める。<br>子宮口を刺激されたナイアは未知の感覚に翻弄されていた。": "Tôi dồn sức thúc sâu quy đầu chạm thẳng vào miệng tử cung.<br>Bị kích thích tận nơi sâu kín, Naia đắm chìm trong khoái cảm lạ lẫm.",
    "だ、だめ、きちゃう……きちゃうよぉ！<br>司令官さん――！　ああぁぁっ、ふぅ――私、いっちゃ――！": "K-Không được rồi, em sắp... em sắp ra rồi!<br>Anh Tư lệnh ơi――! Aaaa, phù―― em ra――!",
    "下腹部が熱くなっているのはこちらも同じだった。<br>お互いの手を握り合いながら、頂点へ駆け上がっていく。": "Hạ bộ tôi cũng nóng rực như thiêu như đốt.<br>Cả hai nắm chặt tay nhau cùng phi nước đại lên đỉnh vinh quang.",
    "だ、だめっ……！　あああっ！　あんっ、きゃぁう！<br>もっ……あ、いくっ……いくぅっ……あっ！！": "K-Không được rồi...! Aaa! A, hya!<br>Em... a, ra đây... em lên đỉnh đây... a!!",
    "ああんっ！　あ！　あ！　ああぁぁぁぁぁあああぁぁんんん！！！": "Aaa! A! A! Aaaaaaaaaa...!!!",
    "今までで一番大きな喘ぎ声を聞きながら、膣内へ精液を吐き出す。<br>肉棒が律動するたびに甘い快楽が立ち昇り、全身に鳥肌が立った。": "Lắng nghe tiếng rên lớn nhất, tôi bắn xối xả tinh dịch vào trong.<br>Mỗi nhịp giật của thanh thịt mang lại khoái cảm rợn cả tóc gáy.",
    "はっ、ああっ……すご……おなかのおく、しびれて……<br>んぁぁっ……ジンジン、してるぅ……っ。": "Hà, a... tuyệt quá... sâu trong bụng tê dại đi rồi...<br>Ưm a... tê rần rần hết cả rồi...",
    "絶頂の余韻に身体にひくつかせながら、ナイアが頼りなく呟く。<br>きゅっ、と指に力を込めると、同じ力で握り返された。": "Cơ thể co giật trong dư vị cực khoái, Naia yếu ớt thì thầm.<br>Tôi khẽ siết ngón tay, em cũng đáp lại bằng một cái nắm thật chặt.",
    "はぁ、ふぅ……あったかい。<br>これが精液の味……なのかな……お腹のなか、いっぱい……": "Hà, phù... ấm quá.<br>Đây là cảm giác của tinh dịch sao... đầy ắp trong bụng rồi...",
    "あぁぁ……とっても幸せ……": "A... hạnh phúc quá chừng...",
    "司令官さんに、出会えてよかったぁ……": "Gặp được anh Tư lệnh thật là tuyệt vời...",
    "穏やかな笑みを向けられて、こちらの胸も幸福で満たされていた。<br>そうして幸せを分かち合いながら、しばらくの間、見つめ合うのだった――": "Nhìn nụ cười dịu dàng của em, lòng tôi tràn ngập hạnh phúc.<br>Cứ thế chia sẻ khoái cảm ngọt ngào, hai chúng tôi nhìn nhau say đắm――"
}

# ==============================================================================
# HMR_11030100013 (Naia 1 Epilogue)
# ==============================================================================
translations["hmr_11030100013"] = {
    "んっ……ちゅっ♡": "Ưm... chụt♡",
    "なんだ、まだキスをするのか？": "Sao thế, em vẫn muốn hôn nữa à?",
    "だってぇ、キスすると幸せなんだもん……えへへっ♡": "Tại vì hôn anh làm em thấy hạnh phúc lắm... hi hi♡",
    "でも、なんだか幸せすぎて怖いかも……<br>不幸なことが起こらないといいけどなぁ～……": "Nhưng mà hạnh phúc quá thế này lại thấy hơi sợ...<br>Mong là không có chuyện xui xẻo nào xảy ra tiếp theo...",
    "おいおい、やめてくれよ。<br>そんなこと言っていると本当に――ん？": "Này này, đừng nói gở chứ.<br>Em mà nói thế là linh ứng thật đấy―― hm?",
    "ナイア～～。どこ～～～～？<br>もう、ねんねのじか～～～～ん。": "Naia ơiiiii. Ở đâu thếeee?<br>Đến giờ đi ngủ rồiiiii.",
    "あ、フェルちゃん。<br>そっか、私のこと探して――": "A, bé Fortuna.<br>Ra là con bé đang tìm mình――",
    "クンクン――ん～～？<br>ここのへやに、ナイアいる……？": "Hít hít―― ưm~~?<br>Naia ở trong phòng này đúng không...?",
    "……やばくないか。": "...Thế này có nguy hiểm quá không.",
    "や、やばいかもっ？": "Ng-Nguy to rồi chứ lị!?",
    "んぅ？　あかない～？<br>ナイア～、あけてー。": "Ủa? Không mở được~?<br>Naia ơi~, mở cửa đi mà~.",
    "ま、待ってフェルちゃん！<br>これには事情が……！": "K-Khoan đã Fortuna ơi!<br>Chuyện này có uẩn khúc mà...!",
    "あ、バカ！　そんなに慌てると――": "Á ngốc quá! Cuống lên như thế là――",
    "ぎゃんっ！？": "Oái!?",
    "どわーっ！？": "Ối trời ơi!?",
    "あたた、ごめんなさい……って、しし、司令官さん！<br>こんな、押し倒されてるところをフェルちゃんに見られたら……！": "Ui da, em xin lỗi... mà khoan, anh Tư lệnh ơi!<br>Cảnh này mà để Fortuna thấy thì...!",
    "押し倒したわけじゃない！<br>そっちが急に転ぶから！": "Anh có đè đâu!<br>Tại em tự nhiên vấp ngã đấy chứ!",
    "ナイア～？　ころんだ？　だいじょうぶ？<br>いま、ドアこわして、そっちいくっ。": "Naia ơi~? Ngã hả? Có sao không?<br>Chờ xíu, em phá cửa vào cứu Naia liền.",
    "はわわわっ、待って！<br>子どもは見ちゃいけない状況だから～～！": "Oa oa oa, khoan đã!<br>Cảnh này trẻ con không được xem đâuuu~!",
    "（さっそく不幸なこと、起こったなぁ……ははは）": "(Vừa dứt lời là điềm xui tới liền luôn... ha ha ha)"
}

# ==============================================================================
# HMR_11030100021 (Naia 2 Intro)
# ==============================================================================
translations["hmr_11030100021"] = {
    "（う、う～ん……司令官さんの役に立ちたくて<br>娼館で働きたいなぁ～！！　って言ってみたけど――）": "(Ư... mình muốn giúp ích cho anh Tư lệnh<br>nên mới bảo 'em muốn làm việc ở kỹ viện'~!! Cơ mà――)",
    "（どどど、どうしよう！　娼館なんて初めてだから<br>どんなふうに接客すればいいのかわからないよぉ～！）": "(L-Làm sao bây giờ! Kỹ viện là nơi mình chưa từng tới,<br>hoàn toàn chẳng biết phải tiếp khách thế nào cả~!)",
    "い、いらっしゃいませー！<br>今夜は料理ではなくナイアシェフのことを召し上がってくださ～～い！": "K-Kính chào quý khách ạ!<br>Tối nay xin đừng nếm món ăn, mà hãy 'xơi' bếp trưởng Naia điii~!",
    "――とかかな？<br>いや、流石に違うよね……あはは。": "――Nói thế được không ta?<br>Thôi thôi, chắc chắn không phải thế rồi... a ha ha.",
    "あらあら。お悩みみたいね。": "Ô kìa ô kìa. Xem ai đang đau đầu kìa.",
    "あ、ルディアさん！<br>ごめんなさい、うるさかったですか……？": "A, chị Lydia!<br>Em xin lỗi, em có làm ồn quá không ạ...?",
    "全然。それより、接客についてのアドバイスなんだけど――<br>フェルトゥーナさんにいつも接するみたいにしてみたらどうかしら？": "Không hề. Mà này, chị có lời khuyên về cách tiếp khách này――<br>Em cứ đối xử như cách em hay chăm sóc bé Fortuna xem sao?",
    "え？　フェルちゃん？<br>どうしてです？": "Dạ? Bé Fortuna á?<br>Tại sao lại thế ạ?",
    "フェルトゥーナさんと話すときのナイアさんは、<br>とっても優しくてお母さんみたいだもの。": "Vì những lúc nói chuyện với Fortuna, Naia dịu dàng lắm,<br>trông chẳng khác nào một người mẹ hiền vậy.",
    "えぇぇ……。私は別にそういうつもりないんだけどなぁ……<br>でも、それが接客にどう活かせるんですか？": "Eh... em đâu có cố ý như thế đâu ạ...<br>Nhưng mà làm thế thì giúp ích gì cho việc tiếp khách ạ?",
    "ふふっ。実は、お客様ってママさんプレイが好きな人が多いの。<br>その母性は絶対武器になるわ。": "Hi hi. Thật ra khách đến đây nhiều người thích trò mẹ con lắm.<br>Bản năng làm mẹ ấy đảm bảo sẽ là vũ khí tối thượng của em.",
    "ちょうど、ナイアさんが今回お相手するお客様も<br>そういった趣向をお持ちなの――試してみてもらえる？": "Vừa hay vị khách lần này của Naia cũng có sở thích như thế――<br>Em thử một phen xem sao nhé?",
    "う、うーん……わ、わかりました！<br>他にアイディアもないし、やってみます……！": "Ưm... v-vâng ạ!<br>Đằng nào cũng hết cách rồi, em sẽ cố thử xem sao...!",
    "――方針を決めたナイアは、<br>部屋で待つ客の元へ向かうのだった。": "――Sau khi xác định phương châm, Naia bước về căn phòng<br>nơi vị khách đang chờ đợi."
}

# ==============================================================================
# HMR_11030100022 (Naia 2 H-scene)
# ==============================================================================
translations["hmr_11030100022"] = {
    "寝そべる客に寄り添うようにして座ったナイア。<br>彼女の下着はすでに脱ぎ捨てられ、その美しい乳房を男の目に晒していた。": "Naia ngồi nép sát bên vị khách đang nằm dài trên giường.<br>Nội y đã cởi bỏ, để lộ cặp tuyết lê tuyệt mỹ trước mắt gã.",
    "彼女は客の希望に応え、その男性器を優しく握る。<br>肉棒は既に硬直し、雄々しく反り返っていた。": "Chiều theo ý khách, em nhẹ nhàng nắm lấy dương vật của gã.<br>Thanh thịt đã cương cứng từ lâu, ngóc đầu kiêu hãnh.",
    "こ、こんな体勢でよろしいでしょうかっ？": "T-Tư thế thế này đã vừa ý anh chưa ạ?",
    "ナイアが緊張した声で問い掛けるが、<br>客からの答えはない。": "Naia cất giọng run run hỏi,<br>nhưng vị khách không đáp lời.",
    "……あの？": "...Anh ơi?",
    "戸惑っていると、ママ……と、期待の視線を向けながら呟かれた。<br>既に、客はプレイに入り切っているらしい。": "Đang bối rối thì gã nhìn em đầy mong đợi thốt lên 'Mẹ ơi...'.<br>Có vẻ vị khách đã nhập tâm hoàn toàn vào vai diễn.",
    "（マ、ママかぁ……やっぱりこの歳でママはちょっとなぁ……）": "(M-Mẹ sao... tuổi này mà xưng mẹ thì có hơi ngại quá...)",
    "内心、複雑なナイア。だが、客はそれを敏感に感じ取ったのか<br>すぅ――っと冷めた表情になっていく。": "Trong lòng Naia rối bời. Nhưng vị khách dường như nhận ra<br>nên nét mặt gã bỗng lạnh dần đi.",
    "（あ、だめだ……！　お客さんはお金も払ってるんだし<br>たくさんサービスしないと……！）": "(A, không được rồi...! Khách đã trả tiền đàng hoàng,<br>mình phải phục vụ thật chu đáo mới được...!)",
    "料理と同じだ。客の注文に応えるのは基本中の基本にして神髄。<br>挽回しなくてはならない。ルディアの言葉を思い返す。": "Cũng giống nấu ăn, đáp ứng đúng yêu cầu của khách là trên hết.<br>Phải gỡ gạc lại thôi. Em nhớ lại lời dặn của Lydia.",
    "（えっと、えとえと……<br>フェルちゃんに接するように、だったよね！）": "(Để xem nào, xem nào...<br>Phải dỗ dành như đối với bé Fortuna đúng không!)",
    "は～～い、ママですよ～～。": "Vâaang, mẹ đây rồi nè con ngoan~~.",
    "ナイアは必死に笑顔を取り繕い、その声色にも気を配った。<br>精一杯に優しい声を作って、男に語り掛ける。": "Naia cố nặn ra nụ cười và chỉnh lại ngữ điệu của mình.<br>Em dùng chất giọng dịu dàng nhất để dỗ dành gã đàn ông.",
    "今日も頑張ってたね、よしよし♪<br>ママがたくさんご褒美あげるからね～。": "Hôm nay con cũng ngoan lắm, ngoan nào ngoan nào♪<br>Mẹ sẽ thưởng cho con thật nhiều nhé~.",
    "甘やかされた客は頬を緩め、本当の赤子のように喜ぶ。<br>実に満足そうだ。": "Được cưng nựng, vị khách giãn cơ mặt vui sướng như đứa trẻ.<br>Trông gã vô cùng thỏa mãn.",
    "（フェルちゃんを甘やかすときより大げさにしてみたけど<br>これがいいんだ……よし、この調子で……！）": "(Dù diễn hơi lố hơn lúc dỗ Fortuna một chút,<br>nhưng hiệu quả thật... Tốt, cứ thế phát huy...!)",
    "さらに満足してもらえるようにナイアは次の行動へ移る。<br>肉棒に絡めていた指へ、わずかに力をこめた。": "Để làm khách hài lòng hơn, Naia chuyển sang bước tiếp theo.<br>Những ngón tay em khẽ siết nhẹ quanh thanh thịt.",
    "それじゃあ、さっそく……<br>ママのおててで、おちんちんよしよし……してあげるね。": "Vậy thì bây giờ...<br>để tay mẹ xoa xoa cho chim ngoan của con nhé.",
    "よ～し、よ～し……": "Ngoan nào~ ngoan nào~...",
    "肉棒をそっとさするように愛撫する。<br>頭も一緒に優しく撫でると、男はくすぐったそうに目を細めた。": "Em nhẹ nhàng vuốt ve thanh thịt.<br>Vừa xoa đầu vừa vuốt ve, người đàn ông sướng râm ran híp mắt lại.",
    "いいこ、いいこ……ん、ふぅ……<br>ボクくんはと～ってもいいこっ。": "Ngoan quá, ngoan quá... ưm, phù...<br>Bé cưng của mẹ thật là ngoan quá đi.",
    "手コキをしている指に力を込めると、小さく吐息が漏れる。<br>肉棒はびくびくと律動して、さらに熱を帯びていった。": "Mỗi nhịp tuốt tay của em làm gã khẽ thở hắt ra.<br>Thanh thịt giật giật nhịp nhàng, ngày càng nóng rực lên.",
    "（あっ、感じてくれてるんだ……）": "(A, anh ấy đang sướng kìa...)",
    "手をゆっくり上下するたび、ママ、ママぁ……と呟きが漏れる。<br>うまくできている――そんな実感を得て、ナイアの緊張も自然とほぐれた。": "Mỗi nhịp tay lên xuống, gã lại rên rỉ 'Mẹ ơi, mẹ ơi...'.<br>Thấy mình làm tốt, sự căng thẳng trong Naia cũng tự nhiên tan biến.",
    "どぉ～？　ママのよしよし……<br>おちんちん、気持ちいいかな～？": "Thế nào nào~? Mẹ xoa xoa thế này...<br>chim nhỏ của con có thấy sướng không nè~?",
    "客は答えられず、あぁぁぁっ……とよがっている。<br>腰が浮いてしまいそうになっているのを、必死に押さえている様子だった。": "Vị khách không nói nên lời, chỉ rên rỉ 'Aaaa...'.<br>Hông gã như muốn nhổm dậy nhưng phải cố kìm lại.",
    "うんうん、気持ちよくなれてえらいよ～。すごいすごいっ。<br>ボクくんが感じているところ、もっと見せてね～……ん……": "Đúng rồi, sướng thế là ngoan lắm nha~. Giỏi lắm giỏi lắm.<br>Cho mẹ xem vẻ mặt sướng của bé cưng nhiều hơn nữa nào~... ưm...",
    "そうしたら、ママも嬉しいから……ね？": "Như thế thì mẹ cũng sẽ vui lắm đó... ngoan nhé?",
    "こくこく、とわずかに顎を動かして首肯する男。<br>ナイアの胸にも柔らかく、温かいものが宿る。": "Người đàn ông gật gật đầu đồng ý.<br>Trong lòng Naia bỗng dâng lên một cảm giác ấm áp lạ thường.",
    "（なんだか、可愛くなってきちゃった……<br>やっぱり私、ちょっとママっぽいのかなぁ？）": "(Tự nhiên thấy anh ấy dễ thương ghê...<br>Không lẽ mình thực sự có phong thái làm mẹ sao ta?)",
    "微笑みながら手コキを続けていたのだが、ふと男の視線が<br>とある場所に集中しているのに気が付く。潤んだ瞳で、じっと見ている。": "Đang mỉm cười sục cu tiếp, em chợt nhận ra ánh mắt của gã<br>đang dán chặt vào một điểm. Đôi mắt ngấn nước nhìn chằm chằm.",
    "ん～～？　ママのおっぱい、吸いたい？": "Hửm~~? Muốn ti sữa mẹ hả con?",
    "――こくんっ、と恥ずかしそうに男は頷く。<br>だが、期待しているのは手に取るようにわかった。": "――Người đàn ông bẽn lẽn gật đầu.<br>Sự thèm muốn lộ rõ mồn một trong ánh mắt gã.",
    "いいよ……たっくさん、ちゅぱちゅぱしてね～。": "Được chứ... tha hồ bú mút cho đã nhé con yêu~.",
    "びくんっ、と言葉の代わりに肉棒が軽く跳ねて返事をした。<br>ナイア自身もわずかに情欲を胸に灯しながら、乳首を口へあてがいにいく――": "Thanh thịt nảy lên một nhịp thay cho lời đáp.<br>Bản thân Naia cũng nhen nhóm chút dục tình, ghé đầu ti vào miệng gã――",
    "んあっ……んっ……ふぁ……ん……": "Ưm a... ưm... phù... ưm...",
    "思いのほか、乳首を強く吸われてナイアは強張る。<br>男も昂っているのか、軽く痙攣するように震えていた。": "Bị mút đầu ti mạnh hơn tưởng tượng, Naia khẽ cứng người.<br>Gã đàn ông vì quá hưng phấn mà người run lên nhè nhẹ.",
    "ナイアは送り込まれる快楽に耐えつつ、奉仕を続けた。<br>男の荒い鼻息が乳房に当たり、くすぐったさを感じながらも手を動かす。": "Naia vừa chịu đựng khoái cảm vừa tiếp tục phục vụ.<br>Hơi thở phì phò của gã phả vào ngực làm em nhột nhưng tay vẫn đưa đều.",
    "んっ、ふぅ……はぁ……どぉ～？　ママのおっぱい、おいちい……？": "Ưm, phù... hà... thế nào~? Sữa mẹ có ngon không nè~?",
    "ふんふん、と切なく繰り返される鼻息で返事をされる。<br>健気な仕草が、じゅわっ、とナイアの胸に情欲を広げていく。": "Tiếng thở gấp gáp của gã như lời khẳng định.<br>Điệu bộ như con nít ấy khiến ngọn lửa dục vọng lan tỏa trong Naia.",
    "ふふっ、ボクくんに喜んでもらえて……ママも嬉しい♡": "Hi hi, làm bé cưng thích thế này... mẹ cũng vui lắm♡",
    "事実、ナイアも悦んでいた。男からは見えていないが<br>割れ目から愛液がにじみ、太ももを濡らしてしまっている。": "Thực sự Naia cũng đang sướng. Dù gã không nhìn thấy<br>nhưng dâm dịch nơi hạ bộ em đã rỉ ra ướt đẫm cả bắp đùi.",
    "た～んと味わってね……お残しは、めっ、でちゅからね～～。": "Bú cho no nê nhé... bỏ mứa là mẹ mắng đó nha~~.",
    "甘く囁きながら、乳首を口に含ませた状態での手コキを繰り返す。<br>単純な往復運動だが、これが男を悦ばせていた。": "Vừa thì thầm ngọt ngào vừa cho gã ngậm ti sục cu liên hồi.<br>Những động tác đơn giản ấy lại khiến gã sướng mê tơi.",
    "肉棒は限界まで膨張して、びくびくびく、と律動した。<br>先走りが幹の部分まで垂れて、ナイアの綺麗な指を汚している。": "Thanh thịt trướng to hết cỡ, giật thắt từng cơn liên tục.<br>Tinh dịch rỉ ra chảy dọc thân cặc làm ướt ngón tay xinh của Naia.",
    "にっちゅにっちゅの、ぐっちゅぐちゅ……んはぁ……あ……<br>ふふっ、すごいすごい。立派でちゅよっ♪": "Ướt nhẹp nhóp nhép hết cả rồi... haaa... a...<br>Hi hi, giỏi quá giỏi quá. Của con dũng mãnh lắm nha♪",
    "褒められた客は夢心地な様子だ。身体もぶるぶると震わせている。<br>尻の辺りに力を込める男の様子を見て、ナイアは限界を悟った。": "Được khen ngợi, vị khách như bay bổng trên mây, toàn thân run rẩy.<br>Thấy gã gồng cứng mông, Naia biết gã đã chạm tới giới hạn.",
    "ん～？　もしかして、ボクくん……<br>我慢してるんでちゅか？": "Ủa ta~? Không lẽ bé cưng...<br>đang cố nhịn đó hả?",
    "ダメでちゅよ～。ママには、思いっきり甘えないと……ママが、全部受け止めて<br>あげまちゅから♡　だから、たくさん幸せになってくだちゃい♡": "Không được nhịn đâu nha~. Mẹ sẽ hứng trọn cho con hết mà♡<br>Cứ sướng cho thỏa thích đi con yêu♡",
    "慈愛をこめた眼差しで見つめながら、ナイアは彼の頭を愛撫する。<br>男が小さく頷いたのを確認し、陰茎を握る手に力を込めた。": "Dùng ánh mắt đầy từ mẫu vuốt ve đầu gã,<br>thấy gã gật đầu, em liền siết chặt tay sục mạnh hơn nữa.",
    "はぁっ――！　んっ、ん……っ！": "Haaa――! Ưm, ưm...!",
    "ナイアは手淫の周期を早める。快楽を強められた男はとても<br>感じているようで、さらに身を強張らせ、鼻息を荒くした。": "Naia tăng tốc độ quay tay. Khoái lạc dâng trào tột độ làm gã<br>gồng cứng toàn thân, thở dồn dập như bò mộng.",
    "くっ……ふぅううんんっ……！": "Hức... phù ưm...!",
    "身を痙攣させる男は、助けを求めるように乳首を吸い立てた。<br>性感帯を鋭く刺激されたナイアも快感を覚えてしまう。": "Cơ thể co giật, gã như tìm phao cứu sinh ra sức bú ngấu nghiến đầu ti.<br>Bị kích thích mạnh vào điểm nhạy cảm, Naia cũng rên lên vì sướng.",
    "それをいけないことだと思ったのか、客は乳首への刺激を弱めた。<br>そんな男へと、ナイアは微笑みながら語り掛ける。": "Tưởng mình làm sai, vị khách liền nới lỏng miệng ra.<br>Thấy vậy Naia liền mỉm cười dịu dàng bảo:",
    "やぁん……大丈夫でちゅよ、ボクくん……んっ、ふぅ……<br>そのまま……おっぱいにちゅぱちゅぱしてくだちゃい？": "Ư... không sao đâu bé ngoan... ưm, phù...<br>Cứ tiếp tục... mút ti mẹ như thế đi nào con?",
    "ボクくんがどんなことをしても、ママはどこにもいかないから♡<br>安心して、気持ち良くなってくだちゃいね～……はぁ、ふぅ……": "Dù con làm gì mẹ cũng không bỏ đi đâu mà♡<br>Cứ an tâm mà sướng đi nhé con yêu~... hà, phù...",
    "また、ナイアの手中で肉棒が一段と膨らんだ。<br>ナイアは満足感に浸りながら強めの手淫を続ける。": "Thanh thịt trong tay Naia lại nở to thêm một vòng.<br>Em tràn đầy mãn nguyện, tiếp tục dùng sức sục mạnh hơn.",
    "あっ、あっ、あっ……おっぱい吸うの、上手……<br>ちゅぱちゅぱ、おじょーじゅぅ♡　んっ……んんンっ……♡": "A, a, a... bú ti giỏi quá nè...<br>bú mút giỏi lắm nha con yêu♡ Ưm... ưm♡",
    "肉棒と乳首。奉仕と吸引。<br>まるで互いに快楽を分け合うような、信頼に満ちた行為だった。": "Dương vật và đầu nhũ. Phục vụ và mút mát.<br>Cứ như thể cả hai đang san sẻ khoái lạc cho nhau đầy tin tưởng.",
    "ナイアの心からの優しさに包まれ、男は限界に近づいていた。<br>先走りに白濁したものが混ざり始める。": "Được bao bọc bởi sự dịu dàng chân thành của Naia, gã sắp bắn.<br>Những giọt dịch trắng đục bắt đầu rỉ ra ở đầu lỗ sáo.",
    "ああっ、ふぅ……ん～？　ボクくん、白いおしっこ出ちゃいそう？<br>いいでちゅよ♡　たっくさんだちまちょうねー♡": "A, phù... ủa~? Bé cưng sắp tè ra nước màu trắng rồi hả?<br>Được thôi nè♡ Cứ xả ra thật nhiều nhé con♡",
    "ママのおてての中にしーしー、して♡<br>ぜーんぶ、受け止めてあげまちゅから……んはぁ……あっ……♡": "Tè hết vào lòng bàn tay mẹ đi nào♡<br>Mẹ sẽ hứng trọn cho con hết... haaa... a...♡",
    "甘い声で誘われたのが限界だった。男は鼻から一気に酸素を吐き出し<br>ナイアの乳首を今までで一番の力で吸引した。": "Lời mời gọi ngọt ngào là giọt nước tràn ly. Gã thở hắt ra một hơi<br>rồi dùng hết sức bú nghiến lấy đầu ti của Naia.",
    "あっ……うぅんっ……♡　よちよち♡<br>だちて♡　だちて♡　白いおしっこ♡　しー、しー♡": "A... ưm...♡ Ngoan nào ngoan nào♡<br>Xả ra đi♡ nước tiểu màu trắng♡ tè đi nè, tè đi nè♡",
    "んっ、んっ、んっ……あっ、んんんんっ～～っ！": "Ưm, ưm, ưm... a, ưm ưm~~!",
    "猛り切った肉棒から精液が盛大に射出される。<br>独特の香りが室内に広まり、ナイアの鼻先にもまとわりついた。": "Từ thanh thịt cương cứng, tinh dịch bắn tung tóe xối xả.<br>Mùi hương nồng nàn lan tỏa khắp phòng, quẩn quanh nơi cánh mũi Naia.",
    "甘イキしていたナイアは精液の香りを吸い込みながら余韻に浸る。<br>子宮の辺りから甘い痺れが広まり、割れ目からベッドに蜜を滴らせた。": "Naia đạt cực khoái nhẹ cũng hít hà mùi tinh dịch đắm chìm dư vị.<br>Cơn tê dại lan khắp tử cung khiến dâm dịch nhỏ giọt xuống đệm.",
    "はぁ……はぁ……全部、出せまちたか？　ボクくん♡": "Hà... hà... con xả ra hết sạch chưa hả bé cưng♡",
    "息を早くしながらも、ナイアは男と視線を結び合わせていた。<br>その慈愛に満ちた微笑みに溶かされるように男の表情はだらしなくなっていく。": "Dù thở dốc nhưng Naia vẫn nhìn thẳng vào mắt gã.<br>Trước nụ cười nhân từ, gương mặt gã đàn ông giãn ra đầy thỏa mãn.",
    "そうでちゅか♡　たくさん、しーしーできてえらいでちゅね……♡<br>気持ち良くなれて、本当にえらい♡　よしよし……いい子ぉ、いい子ぉ～♡": "Vậy hả con♡ Tè ra được nhiều thế này giỏi quá...♡<br>Sướng được thế này là ngoan lắm♡ Ngoan nào ngoan nào~♡",
    "最後の最後まで、客を甘やかせる。<br>男はいつまでも幸せそうに目を細めるのだった。": "Cho đến tận giây phút cuối cùng em vẫn cưng chiều khách.<br>Người đàn ông híp mắt ngập tràn trong niềm hạnh phúc vô tận."
}

# ==============================================================================
# HMR_11030100023 (Naia 2 Epilogue)
# ==============================================================================
translations["hmr_11030100023"] = {
    "はーっ……やりきった～～！！": "Haaa... làm xong rồi~~!!",
    "（プレイ中はよかったけど……思い返すと恥ずかしいなぁ……）": "(Lúc làm thì hăng hái thế thôi chứ... nghĩ lại ngượng chết đi được...)",
    "（やっぱり、普通のプレイができるようになった方がいいよね！<br>うん！　絶対にそう！　よし！　頑張ろう～～！）": "(Quả nhiên mình vẫn nên học cách phục vụ bình thường thì hơn!<br>Ừm! Chắc chắn là vậy rồi! Được! Cố lên nào~~!)",
    "あ、ナイアさん！　大変！　大変よ！": "A, Naia ơi! Nguy rồi! Chuyện lớn rồi nè!",
    "ナイアさんにママプレイをしてほしいって<br>お客様が殺到してるの！　よかったわねぇー♪": "Khách kéo đến nườm nượp đòi Naia đóng vai mẹ con kìa!<br>Tuyệt quá còn gì nữa♪",
    "えっ！？<br>なななっ、なんでそんなことに～！？": "Eh!?<br>S-Sao lại thành ra nông nỗi này chứ~!?",
    "きっと、さっきのお客様がナイアさんの良さを<br>あちこちで宣伝してくれたのよ。": "Chắc chắn là vị khách vừa rồi đã đi khắp nơi<br>khen ngợi sự tuyệt vời của Naia đấy.",
    "これで、あなたも立派な娼館の一員ね♪<br>悩みも解決したんじゃないかしら？": "Thế là em đã chính thức thành nhân tố cốt cán của kỹ viện rồi♪<br>Nỗi lo lắng cũng được giải quyết rồi còn gì?",
    "え、えと、それは、確かにそうなんですけど……": "Ơ, ừm, đúng là thế thật nhưng mà...",
    "あの、でも私、できれば普通の……！": "Nhưng mà em muốn làm dịch vụ bình thường cơ...!",
    "きっと、たくさんのお客様に悦んでいただけるわ。<br>司令官くんも喜ぶんじゃないかしら。": "Chắc chắn sẽ làm hài lòng bao nhiêu khách cho xem.<br>Cậu Tư lệnh cũng sẽ vui lây đấy chứ.",
    "うぐっ！？<br>う、ううぅ……！": "Hự!?<br>Ư... ư ư ư...!",
    "うわあああんんん～～っ！　嬉しいけど、嬉しいけどぉ～！！<br>不幸だよぉ～～～！！！": "Oa a a a~~! Vui thì vui thật đấy nhưng mà~~!!<br>Xui xẻo quá đi mất thôi~~~!!!"
}

# ==============================================================================
# HMR_11030100031 (Naia 3 Intro)
# ==============================================================================
translations["hmr_11030100031"] = {
    "ふんふんふーん♪<br>お料理、お料理、楽しいな～♪": "Hừm hừm hừm~♪<br>Nấu ăn, nấu ăn, vui quá đi thôi~♪",
    "ずいぶんとご機嫌だな、ナイア。": "Tâm trạng vui vẻ dữ ta, Naia.",
    "あ、司令官さん！<br>もう来てくれたのっ？": "A, anh Tư lệnh!<br>Anh đã tới rồi đấy à?",
    "あぁ。新作レシピをごちそうしてもらえるって言うからさ。<br>待ち切れなくて、早めに来てしまった。": "Ừ. Nghe bảo được thưởng thức công thức món mới của em mà.<br>Không đợi nổi nên anh mò sang sớm luôn.",
    "そっかぁ～。じゃあ、ちょっと急いで準備するね♪": "Thế ạ~. Vậy em sẽ nhanh tay chuẩn bị ngay đây♪",
    "ふふっ、今回のレシピは自信作だよ。<br>きっと司令官さんも好きだと思うんだぁ～。": "Hi hi, món lần này là tác phẩm tâm đắc của em đấy.<br>Em tin chắc là anh Tư lệnh cũng sẽ mê cho xem~.",
    "（……ふむ。さすがにプロの料理人だけあって、手際がいいな。<br>無駄がないし、手付きも鮮やかだ）": "(...Hừm. Đúng là đầu bếp chuyên nghiệp, thao tác nhanh thoăn thoắt.<br>Động tác dứt khoát không thừa thãi chút nào)",
    "（もちろん味も良いし……ナイアがお嫁さんになったら<br>毎日おいしい料理が食べられて幸せだろうな……）": "(Đồ ăn lại ngon... Nếu Naia mà làm vợ mình,<br>ngày nào cũng được ăn ngon thế này thì hạnh phúc biết mấy...)",
    "（……いかん。想像していると、なんだか抱きたくなってきた……。<br>ちょっとだけなら――触ってもいいか）": "(...Không xong rồi. Càng tưởng tượng lại càng muốn ôm em...<br>Chỉ sờ một chút thôi chắc không sao đâu nhỉ)",
    "……きゃっ？": "...Á?",
    "し、司令官さん？　なんで急にお尻を……あっ♡": "A-Anh Tư lệnh? Sao tự nhiên lại bóp mông em... a♡",
    "あ～……こら。料理中だから危ないよ～。": "A... nè anh. Em đang nấu nướng nguy hiểm lắm đấy~.",
    "それはわかっているんだが、すまん……。<br>料理をしているナイアを見たら、なんか、つい――": "Anh biết chứ, xin lỗi em...<br>Nhìn Naia đứng bếp đảm đang thế này, anh bất giác――",
    "もうっ。えっちなんだから……やんっ……": "Thật là. Anh dê xồm ghê á... a nhược...",
    "（別に嫌がってはいないみたいだな――<br>それなら、このまま……）": "(Có vẻ em ấy không hề ghét――<br>Thế thì cứ tiếp tục luôn vậy...)",
    "はんっ……んぅ……もぉ～。<br>お料理できないってばぁ～……ふふふっ。": "Haa... ưm... thật là~.<br>Thế này sao em nấu nướng được nữa đây~... hi hi hi.",
    "まるで、新婚夫婦のようなやり取りに胸が熱くなる。<br>そのまま彼女の服へと手をかけた――": "Những cử chỉ tình tứ như vợ chồng son làm lòng tôi rạo rực.<br>Tôi liền đưa tay cởi bỏ trang phục của em――"
}

# ==============================================================================
# HMR_11030100032 (Naia 3 H-scene)
# ==============================================================================
translations["hmr_11030100032"] = {
    "キッチンに立つナイアの衣服を下ろし、<br>瑞々しい桃尻に触れる。": "Tôi kéo váy Naia đang đứng trong bếp xuống,<br>chạm tay vào bờ mông đào căng mọng nước.",
    "張りがあるお尻は柔らかさを伴っていて、触るだけで幸せな気分になれた。<br>我慢ができず両手の指を沈み込ませると、心地の良い弾力が返ってきた。": "Bờ mông săn chắc mềm mại, chỉ chạm vào thôi đã thấy hạnh phúc.<br>Không nhịn được, tôi bóp mạnh làm thịt mông nảy lên đàn hồi.",
    "もぉ～～……司令官さんったらぁ……あんっ……": "Thật là~~... anh Tư lệnh hư quá đi... a...",
    "ナイアはどこか楽しそうに、余裕のある笑みを浮かべている。<br>こちらも尻を味わう手が止められない。": "Naia tỏ vẻ thích thú, nở nụ cười đầy nuông chiều.<br>Tay tôi cũng không thể dừng xoa nắn bờ mông em.",
    "ん、ふふ……<br>ご飯の前に、私のことが食べたくなっちゃったの？": "Ưm, hi hi...<br>Chưa ăn cơm mà anh đã muốn 'xơi' em trước rồi sao?",
    "――食べたくなったらダメか？<br>尻揉みを続けながら尋ねると、ナイアは穏やかに同意してくれる。": "――Muốn ăn em trước không được à?<br>Vừa xoa mông vừa hỏi, Naia liền dịu dàng chiều lòng tôi.",
    "いいよ……お召し上がりください……": "Được chứ ạ... xin mời quý khách thưởng thức...",
    "甘ったるく、トロみのある声によって肉棒が熱を持ち、硬くなった。<br>反り返った男性器を桜色の割れ目にあてがいにいく――": "Giọng nói ngọt lịm êm ái khiến thanh thịt nóng ran và cương cứng.<br>Tôi đưa dương vật ngóc cao áp thẳng vào khe thịt hồng hào――",
    "はぁ、ん……あっ……ああんっ……ん……ふふ♡": "Hà, ưm... a... a... ưm... hi hi♡",
    "挿入の瞬間、ナイアは身体を丸めて、可愛らしく悶えていた。<br>膣内は愛液にまみれていて、肉棒に心地良く絡み付いてくる。": "Khoảnh khắc đút vào, Naia uốn éo người rên rỉ đầy đáng yêu.<br>Bên trong ngập tràn dâm dịch quấn chặt lấy thanh thịt thật đê mê.",
    "――濡れているじゃないか。<br>声に出して指摘すると、ナイアは小さくぷるりと背中と膣壁を震わせた。": "――Ướt đẫm hết cả rồi này.<br>Tôi khẽ trêu, bờ lưng và thành âm đạo Naia liền khẽ giật giật.",
    "んぅ、はぁ……あんなに触られたら、濡れちゃうのも当然でしょ～？": "Ưm, hà... bị anh sờ soạng thế kia thì ướt là chuyện đương nhiên mà~?",
    "照れくさそうにふわりと笑う。だが、肌はしっとりと汗ばみ<br>膣内も断続的に収縮している。興奮しているのは明らかだった。": "Em cười ngượng ngùng. Nhưng làn da đã rịn mồ hôi<br>và bên trong liên tục co bóp chứng tỏ em đang rất hưng phấn.",
    "はぁ……ぁ、ふぅ……危ないものもあるし……<br>あんまり激しくはダメだからね？": "Hà... a, phù... ở đây có đồ đạc nguy hiểm...<br>nên anh không được làm mạnh bạo quá đâu đấy nhé?",
    "注意しつつも、こちらのことは受け入れてくれる。<br>了解、と返事をしながら腰のピストンを開始した。": "Dù nhắc nhở nhưng em vẫn đón nhận tôi trọn vẹn.<br>Rõ rồi, tôi đáp lời và bắt đầu nhấp hông đưa đẩy.",
    "はぁ……あんっ……あっ……ああっ……": "Hà... a... a... a...",
    "挿し込んだ肉棒で膣内を味わっていく。<br>蜜襞をなぞる度、彼女はびくびくと背中を震わせた。": "Tôi dùng thanh thịt cắm sâu tận hưởng sự ấm nóng bên trong.<br>Mỗi lần cọ xát nếp gấp âm đạo, sống lưng em lại giật giật run rẩy.",
    "あぁぁ……奥……とんとんされてるぅ……きゃぁん♡": "A... sâu bên trong... đang bị thúc thình thịch nè... a nhược♡",
    "恍惚とした表情で、うっとりと呟かれる。<br>心から幸せそうな声のせいでこちらの気分も高まり、男根の硬さが増していく。": "Em thốt lên với nét mặt ngây dại đê mê.<br>Giọng rên hạnh phúc ấy khiến dương vật tôi càng thêm cương cứng.",
    "あ、そこ……んんっ……横も、奥も、手前も……<br>司令官さんのおちんちんが当たるところ、全部気持ちいい……♡": "A, chỗ đó... ưm... bên cạnh, sâu bên trong, cả bên ngoài nữa...<br>Chỗ nào dương vật anh chạm vào cũng sướng tê người...♡",
    "じっくり味わってもらってるみたい……私の、おまんこ……<br>あん……あっ……どう？　おいし？": "Như thể đang được nếm từng chút một vậy... hoa huyệt của em...<br>A... a... thế nào anh? Có ngon không?",
    "――絶品だ。とても気持ちいい。<br>答えた瞬間、じゅんっ、と膣内がいっそう濡れるのがわかった。": "――Tuyệt phẩm. Sướng lắm em ơi.<br>Vừa dứt lời, dâm dịch bên trong em lại tuôn ra ào ạt.",
    "んぁぁあっ……どうしよ……<br>私も、もっとほしくなっちゃったよぉ……っ。": "Ưm a... làm sao bây giờ...<br>Em cũng muốn được anh làm nhiều hơn nữa rồi...!",
    "彼女にそんなつもりはなかったのだろうが、<br>こちらを誘惑してくるには十分なほど破壊力のあるおねだりだった。": "Dù em không cố ý nhưng lời nũng nịu ấy có sức sát thương lớn,<br>khiến tôi không tài nào cưỡng lại nổi.",
    "とろとろの腟内もまた、ねだるように肉棒に吸い付いてくる。<br>もう耐えることはできず、欲望をぶつけるようにナイアへと体重をかける。": "Âm đạo ướt đẫm mút chặt lấy thanh thịt như mời gọi.<br>Không thể nhịn thêm, tôi dồn sức ghì chặt lấy Naia mà thúc tới.",
    "あんっ、あああっ、お尻ぃ……っ……はぁっ、ああっ……♡": "A, a, mông em... hà, a...♡",
    "右手で美尻をもみしだきつつ、ピストンの速度も上げる。<br>行き来するたび、膣内はきゅきゅっと締まり、切なそうに収縮した。": "Tay phải vừa bóp mông vừa tăng tốc độ nhấp.<br>Mỗi nhịp ra vào, bên trong em lại siết chặt lấy tôi đầy khao khát.",
    "あぁあっ、すごい……お腹の中、きゅんきゅんしてる……<br>締まっちゃってるの、わかるぅ……": "A, sướng quá... trong bụng em cứ thắt lại từng cơn...<br>Em cảm nhận được nó đang siết chặt lấy anh này...",
    "奥とんとんされると、甘いびりびりがくるの……んはぁ……<br>手前に戻るときは、背中とお腹の裏側、ぞくぞくする……": "Mỗi lần anh thúc sâu là một cơn tê dại ngọt ngào... haaa...<br>Lúc rút ra thì sống lưng và bụng dưới râm ran sướng run người...",
    "料理人らしく、味わいの深さを説明してくれた。<br>ナイアに与えている快楽の深さが想像できるせいで、もっと乱れさせたくなる。": "Đúng là đầu bếp, em miêu tả khoái cảm sống động như ăn ngon.<br>Biết em sướng nhường nào, tôi càng muốn làm em phát điên hơn.",
    "あっ、あああっ……！<br>そこ……そこ、強くされるの好き……好きだよぉっ……！": "A, aaaa...!<br>Chỗ đó... chỗ đó bị đâm mạnh em thích lắm... thích lắm luôn...!",
    "びくびく、と膣内が収縮して肉棒を追い立ててくる。<br>こちらも気持ちいい、と告げるとナイアは鼻息を荒くした。": "Âm đạo giật thắt từng cơn mút chặt thanh thịt.<br>Nghe tôi bảo anh cũng sướng lắm, Naia thở dồn dập hơn.",
    "えへへ……やっぱりエッチするの幸せぇ……♡": "Hi hi... làm chuyện ấy với anh hạnh phúc thật đấy...♡",
    "自分もだ、ナイアを抱けると幸せになれる――<br>そう告げた瞬間、肉棒の根本を締めていた入り口がぎゅううっと締まった。": "Anh cũng thế, được ôm Naia làm anh thấy hạnh phúc lắm――<br>Tôi vừa dứt lời, cửa mình em liền thít chặt lấy gốc dương vật.",
    "んあっ……ど、どうしよう……今のやり取り……<br>なんだか新婚さんみたい……": "Ưm a... l-làm sao đây... cách nói chuyện vừa rồi...<br>trông cứ như đôi vợ chồng son ấy...",
    "ね、あなた……？": "Nè... mình ơi...?",
    "艶やかな声色で問い掛けられた瞬間、肉棒と心臓がドクンと脈打つのを感じた。<br>もっとナイアを独占したい、味わい尽くしたいという欲が強くなる。": "Nghe giọng gọi ngọt ngào ấy, tim và dương vật tôi đập thình thịch.<br>Dục vọng muốn chiếm trọn Naia bùng cháy dữ dội.",
    "お願い、あなた……もっとして……<br>私、頑張るから……♡": "Xin mình đấy... hãy làm em nhiều hơn nữa đi...<br>Em sẽ cố gắng chiều mình mà...♡",
    "声だけでなく、潤った膣壁でぎゅっと肉棒をくるんで誘われた。<br>拒む理由はない。膣奥に狙いを定めて、最奥を先端で強く押し込む。": "Không chỉ giọng nói, thành âm đạo ướt đẫm cũng siết chặt mời gọi.<br>Chẳng có lý do gì từ chối, tôi thúc mạnh chạm tận đáy sâu.",
    "あああっ♡　あぁぁ♡　あっ、あっ♡": "Aaaa♡ Aaa♡ A, a♡",
    "尻に叩き付けるように腰を突き出し、ナイアの身体を揺らす。<br>突き上げるたびに彼女から汗が弾け、ふわっといい香りがした。": "Tôi đập hông vào bờ mông em thúc liên hồi, làm người em rung lắc.<br>Mỗi nhịp thúc làm mồ hôi em bắn ra, tỏa hương thơm ngát dịu dàng.",
    "もっと快楽を与えたい――実現するために、尻を揉む左手にも力を込める。<br>汗ばんだ尻は指に吸いつき、十分に高まっているのが窺い知れた。": "Muốn làm em sướng hơn nữa, tay trái tôi bóp chặt mông em.<br>Làn da rịn mồ hôi dính lấy ngón tay cho thấy em đã hưng phấn tột độ.",
    "あなた、あなたっ……♡<br>くぅんっ……ふあああんっ……んああっ……！": "Mình ơi, mình ơi...♡<br>Ưm... oa a a... ưm a...!",
    "ナイアから『あなた』と呼ばれるたび、<br>本当に新婚の嫁とセックスをしているような感覚に襲われる。": "Mỗi lần nghe Naia gọi 'mình ơi',<br>tôi có cảm giác như đang ân ái với cô vợ mới cưới thực sự.",
    "胸に宿った愛おしさに反応して、亀頭が膨張するのを感じた。<br>コリッとした子宮口をしっかり刺激できるよう、ピストンに力を込める。": "Đáp lại tình yêu trào dâng trong tim, quy đầu tôi trướng to thêm.<br>Tôi ra sức nhấp hông để kích thích mạnh mẽ vào miệng tử cung.",
    "やぁんっ♡　激しぃ……♡<br>もぉ、激しいのダメって言ったのに……あなたったら♡　あああん♡": "A nhược♡ Mạnh bạo quá...♡<br>Đã bảo không được làm mạnh rồi mà... mình hư quá à♡ Aaa♡",
    "きっと、手が届くなら頭をよしよしと撫でられていたに違いない。<br>それほど、キッチンの中は甘い空気で満たされている。幸せな空間だ。": "Nếu tay với tới được chắc em sẽ xoa đầu tôi khen ngợi mất.<br>Căn bếp ngập tràn không khí ngọt ngào, đong đầy hạnh phúc.",
    "あっ、あっ、ひゃんっ……すごい、すごいすごい……すてき……♡<br>おまんこ、おちんちんに刺されて、ぐずぐずになっちゃってるよぉ♡": "A, a, hya... tuyệt quá, sướng quá đi mất... thích ghê...♡<br>Bướm em bị dương vật của mình cày xới nát bét hết rồi này♡",
    "その変化はこちらも肉棒で感じている。膣内はほどよい弾力を維持したまま<br>完全に勃起した男根を受け入れ、味わっていた。": "Tôi cảm nhận rõ điều đó qua thanh thịt. Bên trong em đàn hồi,<br>ôm trọn và thưởng thức dương vật cương cứng tối đa của tôi.",
    "今ならどれだけ激しくしても、ナイアは受け入れてくれるだろう。<br>結合部から愛液が弾けるほどの勢いで、膣内での往復運動に没頭する。": "Dù tôi có làm dữ dội cỡ nào Naia cũng sẽ đón nhận.<br>Tôi dập hông liên hồi đến mức dâm dịch bắn tung tóe quanh điểm kết nối.",
    "んああっ、あああ、あああっ……♡　本当にすごいっ……♡<br>で、でも、もう……あなた、私、もぉっ、もぉっ……！！": "Ưm a, aaa, aaaa...♡ Tuyệt lắm mình ơi...♡<br>N-Nhưng mà, em... em sắp... sắp không chịu nổi nữa rồi...!!",
    "ナイアは全身を切なく痙攣させている。膣内も連動して細動していた。<br>絶頂が近い。それは、こちらもだった。下腹部では熱が煮えたぎっている。": "Toàn thân Naia run rẩy co giật. Bên trong em cũng co thắt kịch liệt.<br>Em sắp lên đỉnh rồi. Và tôi cũng vậy, luồng nhiệt đang sôi sục.",
    "――こちらも、もうすぐだ。<br>吐息混じりに射精を訴えると、きゅうぅっ、と膣内がまた締まった。": "――Anh cũng sắp ra rồi.<br>Nghe tôi thở hổn hển báo sắp bắn, bên trong em lại siết chặt lấy tôi.",
    "はい♡　あなた……♡　はやく、きて……準備、できてるから……<br>私のなかに……たくさん、びゅるびゅるしてぇ♡　あああ♡": "Vâng♡ Mình ơi...♡ Mau ra đi... em chuẩn bị xong rồi...<br>Bắn thật nhiều... xối xả vào trong em đi mình♡ Aaa♡",
    "許可を得て、ぐつぐつと煮えていた射精感を解き放ち、身を委ねる。<br>内側からせり上がってくる欲望を、そのままナイアの奥へぶちまけていく。": "Được cho phép, tôi thả lỏng giải phóng cơn xuất tinh đang sôi sục.<br>Trút hết toàn bộ dục vọng cuộn trào vào sâu tận cùng bên trong Naia.",
    "あ、やだっ、私、もう……い、いっ、イっちゃ……♡<br>あ、ああっ、あああんんんっ♡": "A, em sắp... em ra... em lên đỉnh đây...♡<br>A, a, aaaaa...♡",
    "ああん♡　あ――んあぁあああああァァアアア～～っ♡♡♡♡": "Aaa♡ A―― aaaaaaaaaaa~~♡♡♡♡",
    "ナイアは全身と膣内を律動させながら、精液を子宮口で受け止めてくれた。<br>びゅくっびゅくっと肉棒が跳ねるたび、快楽で頭がクラクラした。": "Naia co thắt toàn thân đón trọn dòng tinh dịch nơi miệng tử cung.<br>Mỗi nhịp giật của thanh thịt làm đầu óc tôi quay cuồng trong sung sướng.",
    "は、ああ、はぁぁぁっ……♡<br>くぅん……ふあん……はぁ、はぁあ……♡": "Hà, a, haaa...♡<br>Ưm... phù... hà, haaa...♡",
    "呼吸を整えながら、ナイアは余韻に浸っている。お尻も細かく、<br>ゆらゆら揺れていた。その動きが、最後の一滴まで射精を促してくる。": "Vừa thở dốc Naia vừa đắm chìm trong dư vị cực khoái. Mông khẽ đung đưa,<br>khiến tôi tiếp tục bắn ra từng giọt tinh dịch cuối cùng.",
    "すっごい……いつもより出てる……全然止まらない……♡": "Nhiều quá... bắn ra nhiều hơn mọi khi... mãi không dừng lại luôn...♡",
    "いつもより興奮したから？　ふふっ……司令官さんもそうだったんだ……<br>なんか、新婚さんみたいで……すごかったよね……": "Vì anh hưng phấn hơn mọi khi sao? Hi hi... anh Tư lệnh cũng thế à...<br>Cảm giác như vợ chồng son vậy... tuyệt thật đấy anh nhỉ...",
    "実際、クセになりそうだった。<br>同じ気持ちだったのか、ナイアはくすりと笑う。": "Quả thực tôi sắp nghiện cảm giác này mất rồi.<br>Chắc Naia cũng nghĩ vậy nên em khẽ mỉm cười tinh nghịch.",
    "……続きは、夜のベッドでね……あなた♡": "...Phần tiếp theo để dành tối nay trên giường nhé... mình yêu♡"
}

# ==============================================================================
# HMR_11030100033 (Naia 3 Epilogue)
# ==============================================================================
translations["hmr_11030100033"] = {
    "……よしっ、お料理完成～！　ナイアシェフの<br>『スーパーウルトラジャスティスデリシャスお肉盛り』だよ～！": "...Xong rồi, món ăn đã hoàn thành~! Món thịt siêu cấp<br>vô địch chính nghĩa thơm ngon của bếp trưởng Naia đây~!",
    "おぉ、これはうまそうだ！": "Ồ, trông ngon mắt ghê!",
    "（相変わらず、名前だけはアレだが……）": "(Vẫn như mọi khi, chỉ có cái tên là kỳ quặc...)",
    "ふふっ、味は保証する！<br>ぜぇ～ったい、美味しいよっ！": "Hi hi, em bảo đảm hương vị tuyệt đối!<br>Chắc chắnnn là ngon lắm đấy!",
    "あ、でもなぁ～……司令官さんのせいで形が崩れちゃったよぉ……<br>綺麗に盛り付けてたのにっ。": "A mà... tại anh Tư lệnh mà đĩa thức ăn bị xô lệch hết rồi kìa...<br>Em cất công bày biện đẹp mắt thế mà.",
    "ふむ。なるほど。少し斜めになっているのは俺のせいだったか。": "Hừm. Ra vậy. Bị nghiêng một chút là do lỗi của anh sao.",
    "そうだよ～。あんなに揺らすんだもん……": "Chứ sao nữa~. Tại anh lắc người em dữ dội quá mà...",
    "それは悪かったな。けど、また明日作ればいいだろう？<br>いっそ明日だけじゃなくて、毎日でもいいんだがな……": "Cho anh xin lỗi nhé. Nhưng ngày mai lại làm tiếp là được chứ gì?<br>Mà chẳng riêng ngày mai, ngày nào em làm cũng được hết á...",
    "えっ。それって……": "Eh. Ý anh là...",
    "（まるでプロポーズみたいだけど……そういうこと！？）": "(Nghe chẳng khác nào lời cầu hôn... chẳng lẽ là ý đó thật!?)",
    "ん？　どうした？": "Hm? Sao thế em?",
    "（あ、違うや……。これ何も考えずに言っただけだ。<br>もうっ、司令官さんったら！）": "(A, không phải rồi... Anh ấy chỉ buột miệng nói vu vơ thôi.<br>Thật là, anh Tư lệnh này!)",
    "（……だけど、そんなところも可愛くて好きだなぁ。えへへ）": "(...Nhưng mà tính ngây ngô ấy cũng dễ thương ghê, em thích lắm. Hi hi)",
    "おいおい。本当にどうした。<br>急に黙ったかと思えば、ニヤニヤして。": "Này này. Rốt cuộc em sao thế.<br>Tự nhiên im lặng rồi lại tủm tỉm cười một mình.",
    "ふふっ、なんでもないよ！<br>それより、美味しい？": "Hi hi, không có gì đâu ạ!<br>Mà anh thấy ăn có ngon không?",
    "あぁ、最高だ！": "Ừ, ngon tuyệt đỉnh luôn!",
    "よかった！<br>それじゃあご希望通り、毎日作ってあげるね♡": "Tuyệt quá!<br>Thế thì đúng như anh mong ước, ngày nào em cũng nấu cho anh nhé♡",
    "ナイアは眩しい笑顔を<user>に向ける。<br>彼女に見つめられたまま、最高の料理を味わうのだった――": "Naia nở nụ cười rạng rỡ hướng về phía <user>.<br>Dưới ánh mắt âu yếm của em, tôi thưởng thức món ăn tuyệt hảo――"
}

# ==============================================================================
# GHI VÀ XÁC THỰC
# ==============================================================================
total_files = len(translations)
total_keys = 0
errors = []

for folder, kv in translations.items():
    file_path = NOVELS_DIR / folder / "en.json"
    clean_kv = {}
    for ja, vi in kv.items():
        total_keys += 1
        # 1. Clean
        vi = re.sub(r"^(?:\s*<br\s*/?>)+", "", vi)
        vi = re.sub(r"(?:<br\s*/?>\s*)+$", "", vi)
        vi = re.sub(r"(?:<br\s*/?>\s*){2,}", "<br>", vi)
        
        # 2. Check br count
        br_count = len(re.findall(r"<br\s*/?>", vi))
        if br_count > 1:
            errors.append(f"[{folder}] Quá 1 thẻ <br> ({br_count}): {vi}")
            
        # 3. Check line lengths
        lines = re.split(r"<br\s*/?>", vi)
        for idx, line in enumerate(lines):
            disp = re.sub(r"<[^>]+>", "", line)
            if len(disp) > 70:
                errors.append(f"[{folder}] Dòng {idx+1} dài quá ({len(disp)} ký tự): {line}")
                
        clean_kv[ja] = vi
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(clean_kv, f, ensure_ascii=False, indent=4)
        f.write("\n")
    print(f"Đã ghi: {folder} ({len(clean_kv)} câu)")

print("\n" + "="*50)
print(f"Tổng kết: {total_files} file ({total_keys} câu)")
if errors:
    print(f"CẢNH BÁO ({len(errors)} lỗi):")
    for e in errors:
        print("  -", e)
else:
    print("HOÀN HẢO 100%! Không còn bất kỳ dòng nào vượt quá 70 ký tự và tối đa 1 thẻ <br>.")

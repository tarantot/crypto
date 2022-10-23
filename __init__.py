import os
import sys
import random
from colorama import init
init(autoreset=True)

from .bcolors import Bcolors
from .decoder import Decoder
from .encoder import Encoder
from .key import Key
from .leave import Leave
from .stamp import Stamp
from .fileDecode import FileDecode
from .fileEncode import FileEncode
from .options import Options


if __name__ == "__main__":
    encoder1 = '''Мшл1XcUVя5l«IбЦКеvШ!,ЫJ[И_=amKdTж^пТoGZ/аW?*{Ъ+иЭ)Я69”чхhзЛ<7ь;ъцpNУ»OЖ%щОЁ(Хнu4#~гП}АSюr0ЮДё&e\>2ЬQxэj“дыwtn'P—РRg$вр НГ–DЗHЙ’LБEВ№Сq"йк8тф.iy:M3|CЩЕ`мсk]FЧY-‘fФ@уAо„Bzbs'''
    encoder2 = '''話夜遠温毛父力友園婦灰页若邑甩版肉次印招禸参龙非舌各官生申走舟再苦豕釆存実述効襾式長由舛足赤届而向全乳具捨府刷艮司枚机枝妻貝矛委电治穴定立麦曲宇昔承季河石禾採並皮争聿念至酉見甘角玉成宿因毒州老耒令羊券考艸直宅底田祭交龟制米性臼糸衣卒拝甲呼法目取岩固共供瓜虫行缶武西表担玄件寺虍波刻自网幸危守的豸瓦白血羽里耳泣岸居在受宙板周用果済協身宝放玊巻鸟'''
    encoder3 = '''成放血瓦岩固周式具温矛网長釆田版担婦遠武虍直夜石岸生承羽園板昔居拝立毛話用宿受念非穴並里行在甲衣米委済件宝瓜季的貝赤父危电卒次見捨目呼玊而龟採襾法虫友巻角共臼令守邑玄協白参幸耳述治灰老艸制定舌園官刷供艮机甘印曲宙舟毒羊因招実果甩苦取至申再寺河乳底聿枝枚鸟玉页妻酉皮表由性禾豸州存舛府争糸効若麦考届券龙宅耒交禸自波各肉司足走全祭刻宇西缶身豕泣向'''
    encoder4 = '''捨自缶招灰豕取司周枝角見宅禾舛岩宝河电老祭巻邑採田表血婦念呼龙版禸効刷武固治委遠瓜法羽穴届泣危肉各虍白而向券在貝立虫羊供園共瓦承由衣毛甩印官毒至页受申米耳話成宇里実寺波用述岸夜聿再釆机糸式臼艮襾舟宙走令生乳州宿担友身協行交玊直園非目耒果甘制全皮玄刻幸若考具鸟府昔卒玉放妻参枚居争网赤並舌守甲次長龟西苦麦拝性酉豸矛定的板件艸底曲存石足季父因済温'''
    stamp = Stamp()
    guide = Stamp()
    leave = Leave()
    enc = Encoder()
    print(stamp.label())
    print(guide.info())
    Options.choice()
from underthesea import word_sent
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from lib.classsify.base import Base

class CategoryRent(Base):
	def __init__(self):
		print("initialized CategoryRent")
		text = [
		    (u'Cần tìm nhà từ 2 lầu trở lên hoặc căn hộ 3 phòng ngủ không nội thất (hoặc nội thất cơ bản ), để làm kí túc xá mini cho sinh viên và nhân viên văn phòng. Ai có nhu cầu cho thuê xin liên hệ Vân 0902 817581.', 'ham'),
		    (u'Cho thuê 1 phòng trọ gần cổng đình phong phú - vị trí : khu KDC 175 hẻm 175 ,đường số 2 ,P. Tăng nhơn phú B , Q9', 'ham'),
		    (u'PHÒNG TRỌ CAO CẤP CHO NỮ THUÊ NGAY ĐH NGÂN HÀNG ĐƯỜNG 17 LINH CHIỂU THỦ ĐỨC', 'ham'),
		    (u'HÒNG TRỌ CHO NỮ THUÊ SỐ 10 ĐƯỜNG 17 PHƯỜNG LINH CHIỂU QUẬN THỦ ĐỨC&nbsp; SẮP HOÀN THIỆN. BẮT ĐẦU NHẬN KHÁCH TỪ HÔM NAY.', 'ham'),
		    (u"Can sv ở ghép quan 9", 'ham'),
		    (u'Mình cần 50 bạn tắm bột tắm trắng bên mình nhé ( da đen lì bất chấp hết nha.k trắng hoàn trả lại tiền', 'spam'),
		    (u'Do Tết cần xuất kho lượng hàng lớn làm quà biếu. Chị cần 3 bạn làm việc thời vụ dịp Tết tại Cơ sở kinh doanh của chị', 'spam'),
		    (u"Ấm nước siêu tốc mới 100%1 lít 8 hàng Việt Nam, không phải hàng Trung quốc, bảo đảm an toàn : 100k Mình ở ĐH Ngân hàng, 56 Hoàng diệu 2, thủ đức", 'spam'),
		    (u'Lên đợt 2 nhé mấy bạn.XOÀI NON. bao tươi ngon lun nhé...tối mai mình giao nha đang vận chuyển lên ạ', 'spam'),
		    (u'Cơ hội cho các bạn sv kiếm thêm cuối năm. Mình cần mua xác iphone, smartphone, laptop hư cũ. Ai có comment bên dưới. Xin ad cho mình đăng tin vài ngày.', 'spam')
		]		
		train=[]		
		for sentence_train in text:
			train.append((word_sent(sentence_train[0], format="text"), sentence_train[1]))
		self.classifier = NaiveBayesClassifier(train)
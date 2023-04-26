# 图片验证码

from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=120, font_sizes=[80, ])
image.write('TyelrXixi', 'captcha.png')


# 音频验证
# from captcha.audio import AudioCaptcha
# audio = AudioCaptcha() # 存入音频文件
# audio.write('10086', 'auio.wav')
''
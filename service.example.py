from core.Baas_thread import Baas_thread
from core.config.config_set import ConfigSet
from main import Main


def main():
    main = Main(ocr_needed=["NUM", "Global", "JP"])  # 日服也必须要 Global，否则会崩溃
    config = ConfigSet(config_dir="jp_hoshino")  # 修改为自己的配置目录名
    baas = Baas_thread(config, None, None, None)
    baas.init_all_data()
    baas.ocr = main.ocr  # type: ignore

    baas.thread_starter()


main()

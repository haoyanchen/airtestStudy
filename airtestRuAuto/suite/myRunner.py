from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
import jinja2
import shutil
import os
import io


class CustomAirtestCase(AirtestCase):
    def setUp(self):
        print("custom setup")
        # add var/function/class/.. to globals
        # self.scope["hunter"] = "i am hunter"
        # self.scope["add"] = lambda x: x+1

        # exec setup script
        # self.exec_other_script("setup.owl")
        super(CustomAirtestCase, self).setUp()

    def tearDown(self):
        print("custom tearDown")
        # exec teardown script
        # self.exec_other_script("teardown.owl")
        super(CustomAirtestCase, self).setUp()

    # 我这里是写死的，如果要多机协作，直接传入参数即可
    def run_air(self, root_dir='C:\\Users\\AUSU\\Desktop\\airtestRuAuto\\suite', device=['Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8']):
        # 聚合结果
        results = []
        # 获取所有用例集
        root_log = root_dir + '\\' + 'log'
        # os.path.isdir():用于判断对象是否为一个目录
        if os.path.isdir(root_log):
            # 递归删除文件夹下的所有子文件夹和子文件
            shutil.rmtree(root_log)
        else:
            # 没有就新建log文件夹
            os.makedirs(root_log)
            print(str(root_log) + 'is created')

        # os.listdir：返回指定文件夹包含的文件或文件夹的名字的列表
        for f in os.listdir(root_dir):
            # f是否是以.air为后缀结束
            if f.endswith(".air"):
                # f为.air案例名称：test1.air
                airName = f
                # 拼接(运行脚本路径),airName_path为.air的全路径：C:\Users\Administrator\Desktop\airtestRuAuto\suite\test1.air
                script = os.path.join(root_dir, f)
                print(script)
                # replace:旧换新
                # 日志存放路径：C:\Users\Administrator\Desktop\airtestRuAuto\suite\log\test1
                log = os.path.join(root_dir, 'log' + '\\' + airName.replace('.air', ''))
                # 日志存放名称:C:\Users\Administrator\Desktop\airtestRuAuto\suite\test1.air\log
                log_1 = script + '\\' + 'log'
                print(log)
                if os.path.isdir(log):
                    shutil.rmtree(log)
                else:
                    os.makedirs(log)
                    print(str(log) + 'is created')
                # 报告的存放路径
                output_file = log + '\\' + 'log.html'
                args = Namespace(device=device, log=log_1, recording=None, script=script, compress=10, no_image=None)
                try:
                    run_script(args, AirtestCase)
                except:
                    pass
                finally:
                    # rpt = report.LogToHtml(script, log)
                    # 脚本路径、log路径、脚本名称
                    rpt = report.LogToHtml(script, log_1, script_name=f.replace(".air", ".py"))
                    rpt.report("log_template.html", output_file=output_file)

                    result = {}
                    # 脚本名字
                    result["name"] = airName.replace('.air', '')
                    # 运行结果
                    result["result"] = rpt.test_result
                    # 拼接，生成聚合报告
                    results.append(result)
        # 生成聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root_dir),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("summary_template.html", root_dir)
        html = template.render({"results": results})
        output_file = os.path.join(root_dir, "summary.html")
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)
        print(output_file)


if __name__ == '__main__':
    test = CustomAirtestCase()
    device = ['Android://127.0.0.1:5037/FIFIMFFEPVAIWCU8']
    test.run_air('C:\\Users\\AUSU\\Desktop\\airtestRuAuto\\suite', device)

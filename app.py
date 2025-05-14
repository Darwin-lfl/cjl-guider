import os

import streamlit as st
import base64
from PIL import Image
import io

# 设置页面配置
st.set_page_config(
    page_title="南京长江路文化之旅",
    page_icon="🏮",
    layout="wide",
)

# 自定义CSS样式
st.markdown("""
<style>
    .main {
        background-color: #FFFAF0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFE4B5;
        padding: 10px 20px;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
        color: #8B4513;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF8C00 !important;
        color: white !important;
    }
    .location-header {
        background-color: #FF8C00;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .photo-card {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .video-card {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .ai-guide-card {
        background-color: #E6F7FF;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border-left: 5px solid #1E90FF;
    }
    .section-title {
        color: #FF4500;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .gallery {
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
    }
    .caption {
        font-style: italic;
        color: #666;
        margin-top: 5px;
        text-align: center;
    }
    .intro-text {
        background-color: rgba(255, 140, 0, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .guide-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        float: left;
        margin-right: 15px;
    }
    .guide-text {
        margin-left: 95px;
    }
</style>
""", unsafe_allow_html=True)


# 模拟占位图片生成函数
def get_image_base64(width, height, text):
    img = Image.new('RGB', (width, height), color=(240, 240, 240))
    return f"data:image/png;base64,{base64.b64encode(io.BytesIO().getvalue()).decode()}"


# 定义景点和对应的内容
locations = {
    "南京图书馆": {
        "intro": "南京图书馆是中国创建最早的公共图书馆之一，也是中国第三大图书馆，拥有丰富的古籍和文献资源。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "南京图书馆历史变迁"},
            {"url": "/api/placeholder/640/360", "caption": "馆藏珍本古籍欣赏"}
        ],
        "ai_guide": {
            "name": "书生",
            "avatar": "avatar/刘思礼-数字人形象.png",
            "video_name": "南京图书馆-AI数字人.mp4",
            "intro": "大家好，我是书生，南京图书馆的数字讲解员。作为一名知识的守护者，我可以为您介绍图书馆的历史沿革和珍贵馆藏，带您体验知识的海洋！",
            "speech": "南京图书馆始建于1907年，历经百年沧桑，现已发展成为藏书1000多万册的国家重点图书馆。这里不仅是一个借阅场所，更是一座文化宝库。馆内珍藏了大量珍贵古籍和历史文献，包括1.6万多部善本古籍，其中不乏宋元明清各朝的珍本秘籍。新馆采用现代化的设计理念，将传统与现代完美结合，为读者提供了舒适的阅读环境和便捷的服务。"
        }
    },
    "长江路": {
        "intro": "南京长江路，被誉为“南京第一历史文化名街”，承载着丰富的历史文化内涵。这条街道见证了多个重要历史时期，沿途分布着众多著名的历史文化景点，是南京历史与文化的重要展示窗口。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "长江路历史变迁全景展示，回顾从古代到现代的发展历程"},
            {"url": "/api/placeholder/640/360", "caption": "长江路景点导览，带您领略沿途各景点的独特魅力"}
        ],
        "ai_guide": {
            "name": "史韵",
            "avatar": "avatar/长江路-AI数字人.png",
            "video_name": "长江路-AI数字人.mp4",
            "intro": "大家好，我是史韵，南京长江路的数字讲解员。我将带您穿梭在长江路的历史长河中，领略这里深厚的文化底蕴和独特魅力。",
            "speech": "南京长江路全长约1800米，从明清时期起就是南京的重要区域。这里有中国近代建筑遗存中规模最大、保存最完整的建筑群——总统府，见证了中国近代历史的风云变幻；还有中国三大博物馆之一的南京博物院，馆藏丰富，能让您领略到华夏文明的璀璨。毗卢寺作为金陵名刹，也为长江路增添了一抹宁静的宗教文化色彩。漫步长江路，就仿佛翻开了一部生动的历史画卷。"
        }
    },
    "1912历史街区": {
        "intro": "1912历史街区是以民国文化为主题的商业休闲区，保留了大量民国时期的历史建筑，成为南京夜生活的热门地点。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "1912街区生活体验"},
            {"url": "/api/placeholder/640/360", "caption": "民国文化在现代城市的传承"}
        ],
        "ai_guide": {
            "name": "民民",
            "avatar": "avatar/1912-AI数字人.png",
            "video_name": "1912-AI数字人.mp4",
            "intro": "嗨，我是民民，1912历史街区的数字讲解员。我可以带您领略这里的民国风情和现代时尚的完美融合，体验南京特色的休闲娱乐生活！",
            "speech": "1912历史街区名称源于辛亥革命爆发的年份，这里保留了大量民国时期的历史建筑，经过改造后成为集餐饮、购物、娱乐于一体的时尚休闲区。街区内的建筑多为巴洛克和哥特式风格，与现代元素巧妙融合，营造出独特的民国风情。这里也是南京夜生活的中心，各种特色餐厅、酒吧、咖啡馆等为游客提供丰富的休闲选择。每当夜幕降临，华灯初上，整个街区就会变得格外热闹，是感受南京现代都市魅力的绝佳去处。"
        }
    },
    "六朝博物馆": {
        "intro": "六朝博物馆是展示南京六朝历史文化的专题博物馆，通过珍贵文物和多媒体技术，生动再现了六朝时期的灿烂文明。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "六朝博物馆导览视频"},
            {"url": "/api/placeholder/640/360", "caption": "六朝历史文化讲解"}
        ],
        "ai_guide": {
            "name": "小六",
            "avatar": "avatar/六朝博物馆-AI数字人.png",
            "video_name": "六朝博物馆-AI数字人.mp4",
            "intro": "大家好！我是小六，六朝博物馆的数字讲解员。我对六朝历史和文化了如指掌，可以带您穿越时空，领略建康的繁华与六朝的风采！",
            "speech": "六朝时期的南京，当时称为建康，是东吴、东晋和宋、齐、梁、陈六个朝代的都城，因此被称为'六朝古都'。这一时期，建康城人口超过百万，是当时世界上最大的城市之一。六朝时期的建康城是国际化大都市，中西文化交流频繁，佛教艺术和玉器制作达到了很高的水平。想了解更多关于六朝的历史故事吗？"
        }
    },
    "江苏省美术馆": {
        "intro": "江苏省美术馆是江苏省规模最大的综合性美术馆，收藏了大量江苏地区优秀艺术家的作品，并定期举办各类艺术展览。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "江苏省美术馆馆藏精品欣赏"},
            {"url": "/api/placeholder/640/360", "caption": "艺术家工作室探访"}
        ],
        "ai_guide": {
            "name": "艺艺",
            "avatar": "avatar/江苏省美术馆-AI数字人.png",
            "video_name": "江苏省美术馆-AI数字人.mp4",
            "intro": "你好，我是艺艺，江苏省美术馆的数字讲解员。作为一名艺术爱好者，我可以为您介绍馆内各类艺术流派和作品的特点，带您领略艺术的魅力！",
            "speech": "江苏省美术馆始建于1936年，是华东地区历史悠久的美术馆之一。馆内收藏了近万件艺术作品，包括传统国画、油画、版画、雕塑等多种艺术形式。特别值得一提的是馆内珍藏的许多近现代艺术大师如徐悲鸿、傅抱石、钱松喦等人的代表作品。每年美术馆都会举办数十场各具特色的展览，是艺术爱好者不可错过的文化殿堂。"
        }
    },
    "江宁织造博物馆": {
        "intro": "江南织造博物馆是中国首家展示江南丝织文化的专业博物馆，通过实物展示和互动体验，展现了南京云锦等传统丝织工艺的精湛技艺。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "南京云锦制作工艺展示"},
            {"url": "/api/placeholder/640/360", "caption": "江南丝织文化历史探秘"}
        ],
        "ai_guide": {
            "name": "锦锦",
            "avatar": "avatar/江宁织造博物馆-AI数字人.png",
            "video_name": "江宁织造-AI数字人.mp4",
            "intro": "大家好，我是锦锦，江南织造博物馆的数字讲解员。我精通各种丝织工艺知识，尤其对南京云锦情有独钟，让我带您领略丝织艺术的无穷魅力！",
            "speech": "江南织造是中国古代官办手工业机构，南京是历代江南织造重要的生产地。南京云锦是中国传统丝织工艺的杰出代表，被誉为'中国第一织锦'，已有1500多年历史。传统云锦织造工艺极为复杂，一匹上等云锦需要两名技师协作，每天仅能织2-3厘米，一匹完整的云锦往往需要一年以上的时间才能完成。博物馆内可以看到织工们在传统大型提花织机上展示织造技艺，这是非常珍贵的非物质文化遗产。"
        }
    },
    "总统府": {
        "intro": "南京总统府是中国近代历史上重要的政治遗址，曾是太平天国天王府、两江总督署、中华民国临时政府及国民政府的所在地。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "总统府历史变迁纪实"},
            {"url": "/api/placeholder/640/360", "caption": "总统府文物珍品欣赏"}
        ],
        "ai_guide": {
            "name": "小府",
            "avatar": "avatar/总统府-AI数字人.png",
            "video_name": "总统府-AI数字人.mp4",
            "intro": "大家好，我是小府，南京总统府的数字讲解员。我精通总统府的前世今生，可以为您讲述这里发生的重要历史事件和人物故事！",
            "speech": "南京总统府的历史可以追溯到1392年的明代藩王府，之后历经太平天国天王府、两江总督署、大清皇帝行宫、中华民国临时政府、国民政府等多个历史时期，见证了中国近代史上的风云变幻。这里保存了大量的历史文物和建筑，中西合璧的建筑风格独具特色。在这里，孙中山先生宣誓就任临时大总统，也是当年蒋介石办公的地方。漫步其中，仿佛穿越时空，与历史对话。"
        }
    },
    "毗卢寺": {
        "intro": "毗卢寺位于南京长江路，是南京历史最悠久的佛教寺院之一，以其精美的建筑和深厚的文化底蕴吸引众多游客和信徒。",
        "videos": [
            {"url": "/api/placeholder/640/360", "caption": "毗卢寺佛事活动纪实"},
            {"url": "/api/placeholder/640/360", "caption": "毗卢寺历史文化探秘"}
        ],
        "ai_guide": {
            "name": "觉觉",
            "avatar": "avatar/毗卢寺-AI数字人.png",
            "video_name": "毗卢寺-AI数字人.mp4",
            "intro": "阿弥陀佛，我是觉觉，毗卢寺的数字讲解员。我可以为您介绍寺院的历史沿革、建筑特色和佛教文化，愿您在这里获得心灵的平静与智慧。",
            "speech": "毗卢寺始建于南朝梁武帝时期，距今已有1500多年历史，是南京现存最古老的寺庙之一。寺名'毗卢'取自佛教中的毗卢遮那佛，意为'光明遍照'。寺内保存有众多珍贵的佛教文物和历史遗迹，其中明代铸造的铜钟尤为著名。寺院建筑布局严谨，殿宇巍峨，园林景观精美，体现了传统佛教建筑的特色。每年农历正月十五和四月初八等佛教节日，这里都会举行盛大的法会活动，吸引众多信徒前来参拜。"
        }
    }
}

# 网站标题和介绍
st.markdown("<h1 style='text-align:center; color:#FF4500;'>南京长江路文化之旅 🏮</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
    <div class="intro-text">
        <h3 style='color:#FF8C00;'>🌟 欢迎来到南京长江路文化之旅 🌟</h3>
        <p>长江路是南京的文化枢纽，沿线汇集了众多历史文化景点和现代艺术场所。从六朝博物馆到1912历史街区，从江南织造博物馆到南京图书馆，这条路线串联起南京的过去与现在，展现了这座城市深厚的文化底蕴和现代活力。</p>
        <p>请选择下方的景点，开始您的虚拟文化之旅吧！每个景点都配有精美明信片、旅游视频和AI数字人导游，带您全方位了解南京的文化魅力！</p>
    </div>
    """, unsafe_allow_html=True)

# 创建主标签选择
location_tabs = st.tabs([loc for loc in locations.keys()])

current_directory = os.getcwd()

# 循环显示每个地点的内容
for i, (location_name, location_data) in enumerate(locations.items()):
    with location_tabs[i]:
        # 地点标题和介绍
        st.markdown(f"""
        <div class="location-header">
            <h2>{location_name}</h2>
        </div>
        <div class="intro-text">
            <p>{location_data['intro']}</p>
        </div>
        """, unsafe_allow_html=True)

        # 创建子标签
        absolute_path = os.path.abspath("assets")
        photo_tab, video_tab, guide_tab = st.tabs(["🖼️ 明信片", "🎬 旅游视频", "🤖 AI数字人导游"])
        location_dir = f"assets/{location_name}"

        # 明信片标签内容
        with photo_tab:
            st.markdown("<h3 class='section-title'>精美明信片</h3>", unsafe_allow_html=True)

            # 分两列展示图片
            cols = st.columns(3)
            postcards = [f for f in os.listdir(location_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

            for j, postcard in enumerate(postcards):
                with cols[j % 3]:
                    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
                    st.markdown(f"<div class='image-container'>", unsafe_allow_html=True)
                    st.image(f"{location_dir}/{postcard}", use_container_width=True)
                    st.markdown(f"</div>", unsafe_allow_html=True)
                    st.markdown(f"</div>", unsafe_allow_html=True)

        # 旅游视频标签内容
        with video_tab:
            st.markdown("<h3 class='section-title'>AI生成的景点视频</h3>", unsafe_allow_html=True)
            st.video(data=f"{location_dir}/{location_name}.mp4", format="video/mp4")

        # AI数字人导游标签内容
        with guide_tab:
            ai_guide = location_data["ai_guide"]
            # 添加AI导游视频展示部分
            st.markdown(f"""
                        <div class="ai-guide-card">
                            <h3 class="section-title">遇见您的AI导游：{ai_guide['name']}</h3>
                            <div style="display: flex; margin-bottom: 20px;">
                                <div style="flex: 1;">
                                    <p><strong>导游介绍：</strong>{ai_guide['intro']}</p>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

            # 添加AI导游视频展示
            st.markdown("<h4 style='color:#FF8C00; margin-top:15px;'>🎬 AI导游视频讲解</h4>", unsafe_allow_html=True)

            # 使用列布局让视频和文字并排显示
            video_col, text_col = st.columns([3, 2])

            with video_col:
                # 插入AI导游视频
                if ai_guide['video_name']:
                    st.video(data=f"{location_dir}/{ai_guide['video_name']}", format="video/mp4")
            with text_col:
                st.markdown(f"""
                            <div style="background-color:#FFF8DC; padding:15px; border-radius:10px; height:100%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                                <h4 style="color:#FF8C00;">导游讲解内容</h4>
                                <p>{ai_guide['speech']}</p>
                            </div>
                            """, unsafe_allow_html=True)

            # 互动问答部分
            st.markdown("<h4 style='color:#1E90FF;'>💬 与AI导游互动</h4>", unsafe_allow_html=True)
            user_question = st.text_input(f"向{ai_guide['name']}提问:", key=f"question_{location_name}")
            if st.button("发送问题", key=f"ask_{location_name}"):
                if user_question:
                    st.markdown(f"""
                                <div style="background-color:#FFEBCD; padding:10px; border-radius:10px; margin-top:10px;">
                                    <p><strong>您的问题:</strong> {user_question}</p>
                                    <p><strong>{ai_guide['name']}的回答:</strong> 感谢您的提问！作为{location_name}的数字导游，我很高兴为您解答关于这里的问题。由于我是一个模拟的AI角色，实际上我无法实时回应特定问题，但在真实应用中，我会根据我的知识库来回答您关于{location_name}的历史、文化、建筑特色等各方面的问题。您可以继续浏览网站了解更多信息！</p>
                                </div>
                                """, unsafe_allow_html=True)
                else:
                    st.warning("请输入您的问题")

# 页脚
st.markdown("""
<div style="text-align:center; margin-top:30px; padding:10px; background-color:#FFE4B5; border-radius:10px;">
    <p>© 2025 南京长江路文化之旅 | 一个虚拟旅游项目</p>
</div>
""", unsafe_allow_html=True)

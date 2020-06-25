/** !
 *	indexjs
 */

(function() {

    // 渲染图表
    var myChart = null;

    function createEAreaChart(conf) {
        myChart = echarts.init(document.getElementById(conf.selector));
        var legendData = []
        for (var i = 0; i < conf.data.series.length; i++) {
            legendData.push(conf.data.series[i].name)
        }
        myChart.setOption({
            color: ['#57a3f1', '#5bd18b', '#ffc349', '#ff7979', '#4491e1', '#e4edf7', '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],
            title: {
                text: conf.data.text,
                textStyle: {
                    color: '#666',
                    fontWeight: 'normal',
                    fontSize: '16px'
                }
            },
            grid: {
                x: 50,
                x2: 30,
            },
            tooltip: {
                trigger: 'axis',
                feature: {
                    dataZoom: {
                        yAxisIndex: 'none'
                    },
                    restore: {},
                    saveAsImage: {}
                }
            },
            legend: {
                y: 'top',
                data: legendData
            },
            xAxis: [{
                type: 'category',
                boundaryGap: false,
                data: conf.data.xAxis,
                axisLine: {
                    show: false
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#eee',
                    }
                }

            }],
            toolbox: {
                show: true,
                feature: {
                    mark: {
                        show: true
                    },
                    dataView: {
                        show: true,
                        readOnly: false
                    },
                    magicType: {
                        show: true,
                        type: ['line', 'bar', 'stack']
                    },
                    restore: {
                        show: true
                    },
                    saveAsImage: {
                        show: true
                    }
                }
            },
            calculable: true,
            yAxis: [{
                type: 'value',
                axisLine: {
                    show: false
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#eee',
                    }
                }
            }],
            series: conf.data.series
        });
    }

    function initEAreaChart(conf) {
        $.ajax({
            url: conf.url,
            type: 'GET',
            dataType: conf.dataType,
            success: function(res) {
                //获取数据成功
                if (res.result) {
                    var data = res.data;
                    createEAreaChart({
                        selector: conf.containerId, // 图表容器
                        data: data, // 图表数据
                    });
                }
            }
        })
    }

    initEAreaChart({
        url: 'https://magicbox.bk.tencent.com/static_api/v3/components/chart1/demo.json',
        dataType: 'json',
        containerId: 'chart_box'
    });

    // 侧栏展开折叠
    var sideBar = $(".bk-sidebar");
    $(".slide-switch").on("click", function() {
        sideBar.toggleClass("slide-open slide-close")
        if (sideBar.hasClass("slide-close")) {
            $(".flex-subnavs").hide();
        }
        setTimeout(function() {
            myChart.resize();
        }, 700);
    });

    // 监听分辨率
    $(window).on('resize', function() {
        var width = $(window).width();
        if (width > 1366) {
            sideBar.removeClass("slide-close").addClass("slide-open");

        } else {
            sideBar.removeClass("slide-open").addClass("slide-close");

        }
        setTimeout(function() {
            myChart.resize();
        }, 700);
    });
    $(window).trigger('resize');
})();
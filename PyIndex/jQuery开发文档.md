

# jQuery API 3.3.1 速查表

[原文链接](http://jquery.cuishifeng.cn/)

## 选择器

- ### 基本

  - [#id](http://jquery.cuishifeng.cn/id.html)
  - [element](http://jquery.cuishifeng.cn/element.html)
  - [.class](http://jquery.cuishifeng.cn/class.html)
  - [*](http://jquery.cuishifeng.cn/all.html)
  - [selector1,selector2,selectorN](http://jquery.cuishifeng.cn/multiple.html)

- ### 层级

  - [ancestor descendant](http://jquery.cuishifeng.cn/descendant.html)
  - [parent > child](http://jquery.cuishifeng.cn/child.html)
  - [prev + next](http://jquery.cuishifeng.cn/next_1.html)
  - [prev ~ siblings](http://jquery.cuishifeng.cn/siblings_1.html)

- ### 基本筛选器

  - [:first](http://jquery.cuishifeng.cn/first_1.html)
  - [:not(selector)](http://jquery.cuishifeng.cn/not_1.html)
  - [:even](http://jquery.cuishifeng.cn/even.html)
  - [:odd](http://jquery.cuishifeng.cn/odd.html)
  - [:eq(index)](http://jquery.cuishifeng.cn/eq_1.html)
  - [:gt(index)](http://jquery.cuishifeng.cn/gt.html)
  - [:lang](http://jquery.cuishifeng.cn/lang.html)1.9+
  - [:last](http://jquery.cuishifeng.cn/last_1.html)
  - [:lt(index)](http://jquery.cuishifeng.cn/lt.html)
  - [:header](http://jquery.cuishifeng.cn/header.html)
  - [:animated](http://jquery.cuishifeng.cn/animated.html)
  - [:focus](http://jquery.cuishifeng.cn/focus_1.html)
  - [:root](http://jquery.cuishifeng.cn/root.html)1.9+
  - [:target](http://jquery.cuishifeng.cn/target.html)1.9+

- ### 内容

  - [:contains(text)](http://jquery.cuishifeng.cn/contains.html)
  - [:empty](http://jquery.cuishifeng.cn/empty_1.html)
  - [:has(selector)](http://jquery.cuishifeng.cn/has_1.html)
  - [:parent](http://jquery.cuishifeng.cn/parent_1.html)

- ### 可见性

  - [:hidden](http://jquery.cuishifeng.cn/hidden_1.html)
  - [:visible](http://jquery.cuishifeng.cn/visible.html)

- ### 属性

  - [[attribute\]](http://jquery.cuishifeng.cn/attributeHas.html)
  - [[attribute=value\]](http://jquery.cuishifeng.cn/attributeEquals.html)
  - [[attribute!=value\]](http://jquery.cuishifeng.cn/attributeNotEqual.html)
  - [[attribute^=value\]](http://jquery.cuishifeng.cn/attributeStartsWith.html)
  - [[attribute$=value\]](http://jquery.cuishifeng.cn/attributeEndsWith.html)
  - [[attribute*=value\]](http://jquery.cuishifeng.cn/attributeContains.html)
  - [[attrSel1\][attrSel2][attrSelN]](http://jquery.cuishifeng.cn/attributeMultiple.html)

- ### 子元素

  - [:first-child](http://jquery.cuishifeng.cn/firstChild.html)
  - [:first-of-type](http://jquery.cuishifeng.cn/firstOfType.html)1.9+
  - [:last-child](http://jquery.cuishifeng.cn/lastChild.html)
  - [:last-of-type](http://jquery.cuishifeng.cn/lastOfType.html)1.9+
  - [:nth-child](http://jquery.cuishifeng.cn/nthChild.html)
  - [:nth-last-child()](http://jquery.cuishifeng.cn/nthLastChild.html)1.9+
  - [:nth-last-of-type()](http://jquery.cuishifeng.cn/nthLastOfType.html)1.9+
  - [:nth-of-type()](http://jquery.cuishifeng.cn/nthOfType.html)1.9+
  - [:only-child](http://jquery.cuishifeng.cn/onlyChild.html)
  - [:only-of-type](http://jquery.cuishifeng.cn/onlyOfType.html)1.9+

- ### 表单

  - [:input](http://jquery.cuishifeng.cn/input.html)
  - [:text](http://jquery.cuishifeng.cn/text_1.html)
  - [:password](http://jquery.cuishifeng.cn/password.html)
  - [:radio](http://jquery.cuishifeng.cn/radio.html)
  - [:checkbox](http://jquery.cuishifeng.cn/checkbox.html)
  - [:submit](http://jquery.cuishifeng.cn/submit_1.html)
  - [:image](http://jquery.cuishifeng.cn/image.html)
  - [:reset](http://jquery.cuishifeng.cn/reset.html)
  - [:button](http://jquery.cuishifeng.cn/button.html)
  - [:file](http://jquery.cuishifeng.cn/file_1.html)

- ### 表单对象属性

  - [:enabled](http://jquery.cuishifeng.cn/enabled_1.html)
  - [:disabled](http://jquery.cuishifeng.cn/disabled_1.html)
  - [:checked](http://jquery.cuishifeng.cn/checked_1.html)
  - [:selected](http://jquery.cuishifeng.cn/selected_1.html)

- ### 混淆选择器

  - [$.escapeSelector(selector)](http://jquery.cuishifeng.cn/jQuery.escapeSelector.html)3.0+

## 核心

- ### jQuery 核心函数

  - [jQuery([sel,[context\]])](http://jquery.cuishifeng.cn/jQuery_selector_context.html)
  - [jQuery(html,[ownerDoc\])](http://jquery.cuishifeng.cn/jQuery_html_ownerDocument.html)1.8*
  - [jQuery(callback)](http://jquery.cuishifeng.cn/jQuery_callback.html)
  - ~~jQuery.holdReady(hold)~~3.2-
  - [jQuery.readyException( error )](http://jquery.cuishifeng.cn/jQuery_readyException.html)3.1+

- ### jQuery 对象访问

  - [each(callback)](http://jquery.cuishifeng.cn/each.html)
  - ~~size()~~1.8-
  - [length](http://jquery.cuishifeng.cn/length.html)
  - [selector](http://jquery.cuishifeng.cn/selector.html)
  - [context](http://jquery.cuishifeng.cn/context.html)
  - [get([index\])](http://jquery.cuishifeng.cn/get.html)
  - [index([selector|element\])](http://jquery.cuishifeng.cn/index_1.html)

- ### 数据缓存

  - [data([key\],[value])](http://jquery.cuishifeng.cn/data.html)
  - [removeData([name|list\])](http://jquery.cuishifeng.cn/removeData.html)1.7*
  - ~~$.data(ele,[key],[val])~~1.8-

- ### 队列控制

  - [queue(e,[q\])](http://jquery.cuishifeng.cn/queue.html)
  - [dequeue([queueName\])](http://jquery.cuishifeng.cn/dequeue.html)
  - [clearQueue([queueName\])](http://jquery.cuishifeng.cn/clearQueue.html)

- ### 插件机制

  - [jQuery.fn.extend(object)](http://jquery.cuishifeng.cn/jQuery.fn.extend.html)
  - [jQuery.extend(object)](http://jquery.cuishifeng.cn/jQuery.extend_object.html)

- ### 多库共存

  - [jQuery.noConflict([ex\])](http://jquery.cuishifeng.cn/jQuery.noConflict.html)

## ajax

- ### ajax 请求

  - [$.ajax(url,[settings\])](http://jquery.cuishifeng.cn/jQuery.Ajax.html)
  - [$.get(url,[data\],[fn],[type])](http://jquery.cuishifeng.cn/jQuery.get.html)
  - [$.getJSON(url,[data\],[fn])](http://jquery.cuishifeng.cn/jQuery.getJSON.html)
  - [$.getScript(url,[callback\])](http://jquery.cuishifeng.cn/jQuery.getScript.html)
  - [$.post(url,[data\],[fn],[type])](http://jquery.cuishifeng.cn/jQuery.post.html)

- ### ajax 事件

  - [ajaxComplete(callback)](http://jquery.cuishifeng.cn/ajaxComplete.html)
  - [ajaxError(callback)](http://jquery.cuishifeng.cn/ajaxError.html)
  - [ajaxSend(callback)](http://jquery.cuishifeng.cn/ajaxSend.html)
  - [ajaxStart(callback)](http://jquery.cuishifeng.cn/ajaxStart.html)
  - [ajaxStop(callback)](http://jquery.cuishifeng.cn/ajaxStop.html)
  - [ajaxSuccess(callback)](http://jquery.cuishifeng.cn/ajaxSuccess.html)

- ### 其它

  - [load(url,[data\],[callback])](http://jquery.cuishifeng.cn/load.html)
  - [$.ajaxPrefilter([type\],fn)](http://jquery.cuishifeng.cn/jQuery.ajaxPrefilter.html)
  - [$.ajaxSetup([options\])](http://jquery.cuishifeng.cn/jQuery.ajaxSetup.html)
  - [serialize()](http://jquery.cuishifeng.cn/serialize.html)
  - [serializeArray()](http://jquery.cuishifeng.cn/serializeArray.html)

## 属性

- ### 属性

  - [attr(name|pro|key,val|fn)](http://jquery.cuishifeng.cn/attr.html)
  - [removeAttr(name)](http://jquery.cuishifeng.cn/removeAttr.html)
  - [prop(n|p|k,v|f)](http://jquery.cuishifeng.cn/prop.html)
  - [removeProp(name)](http://jquery.cuishifeng.cn/removeProp.html)

- ### CSS 类

  - [addClass(class|fn)](http://jquery.cuishifeng.cn/addClass.html)
  - [removeClass([class|fn\])](http://jquery.cuishifeng.cn/removeClass.html)
  - [toggleClass(class|fn[,sw\])](http://jquery.cuishifeng.cn/toggleClass.html)

- ### HTML代码/文本/值

  - [html([val|fn\])](http://jquery.cuishifeng.cn/html.html)
  - [text([val|fn\])](http://jquery.cuishifeng.cn/text.html)
  - [val([val|fn|arr\])](http://jquery.cuishifeng.cn/val.html)

## CSS

- ### CSS

  - [css(name|pro|[,val|fn\])](http://jquery.cuishifeng.cn/css.html)1.9*
  - [jQuery.cssHooks](http://jquery.cuishifeng.cn/jQuery.cssHooks.html)

- ### 位置

  - [offset([coordinates\])](http://jquery.cuishifeng.cn/offset.html)
  - [position()](http://jquery.cuishifeng.cn/position.html)
  - [scrollTop([val\])](http://jquery.cuishifeng.cn/scrollTop.html)
  - [scrollLeft([val\])](http://jquery.cuishifeng.cn/scrollLeft.html)

- ### 尺寸

  - [height([val|fn\])](http://jquery.cuishifeng.cn/height.html)
  - [width([val|fn\])](http://jquery.cuishifeng.cn/width.html)
  - [innerHeight()](http://jquery.cuishifeng.cn/innerHeight.html)
  - [innerWidth()](http://jquery.cuishifeng.cn/innerWidth.html)
  - [outerHeight([options\])](http://jquery.cuishifeng.cn/outerHeight.html)
  - [outerWidth([options\])](http://jquery.cuishifeng.cn/outerWidth.html)

## 文档处理

- ### 内部插入

  - [append(content|fn)](http://jquery.cuishifeng.cn/append.html)
  - [appendTo(content)](http://jquery.cuishifeng.cn/appendTo.html)
  - [prepend(content|fn)](http://jquery.cuishifeng.cn/prepend.html)
  - [prependTo(content)](http://jquery.cuishifeng.cn/prependTo.html)

- ### 外部插入

  - [after(content|fn)](http://jquery.cuishifeng.cn/after.html)
  - [before(content|fn)](http://jquery.cuishifeng.cn/before.html)
  - [insertAfter(content)](http://jquery.cuishifeng.cn/insertAfter.html)
  - [insertBefore(content)](http://jquery.cuishifeng.cn/insertBefore.html)

- ### 包裹

  - [wrap(html|ele|fn)](http://jquery.cuishifeng.cn/wrap.html)
  - [unwrap()](http://jquery.cuishifeng.cn/unwrap.html)
  - [wrapAll(html|ele)](http://jquery.cuishifeng.cn/wrapAll.html)
  - [wrapInner(html|ele|fn)](http://jquery.cuishifeng.cn/wrapInner.html)

- ### 替换

  - [replaceWith(content|fn)](http://jquery.cuishifeng.cn/replaceWith.html)
  - [replaceAll(selector)](http://jquery.cuishifeng.cn/replaceAll.html)

- ### 删除

  - [empty()](http://jquery.cuishifeng.cn/empty.html)
  - [remove([expr\])](http://jquery.cuishifeng.cn/remove.html)
  - [detach([expr\])](http://jquery.cuishifeng.cn/detach.html)

- ### 复制

  - [clone([Even[,deepEven\]])](http://jquery.cuishifeng.cn/clone.html)

## 事件

- ### 页面载入

  - [ready(fn)](http://jquery.cuishifeng.cn/ready.html)

- ### 事件处理

  - [on(eve,[sel\],[data],fn)](http://jquery.cuishifeng.cn/on.html)1.7+
  - [off(eve,[sel\],[fn])](http://jquery.cuishifeng.cn/off.html)1.7+
  - ~~bind(type,[data],fn)~~3.0-
  - [one(type,[data\],fn)](http://jquery.cuishifeng.cn/one.html)
  - [trigger(type,[data\])](http://jquery.cuishifeng.cn/trigger.html)
  - [triggerHandler(type, [data\])](http://jquery.cuishifeng.cn/triggerHandler.html)
  - ~~unbind(t,[d|f])~~3.0-

- ### 事件委派

  - ~~live(type,[data],fn)~~1.7-
  - ~~die(type,[fn])~~1.7-
  - ~~delegate(s,[t],[d],fn)~~3.0-
  - ~~undelegate([s,[t],fn])~~3.0-

- ### 事件切换

  - [hover([over,\]out)](http://jquery.cuishifeng.cn/hover.html)
  - [toggle([spe\],[eas],[fn])](http://jquery.cuishifeng.cn/toggle.html)1.9*

- ### 事件

  - [blur([[data\],fn])](http://jquery.cuishifeng.cn/blur.html)
  - [change([[data\],fn])](http://jquery.cuishifeng.cn/change.html)
  - [click([[data\],fn])](http://jquery.cuishifeng.cn/click.html)
  - [dblclick([[data\],fn])](http://jquery.cuishifeng.cn/dblclick_1.html)
  - ~~error([[data],fn])~~1.8-
  - [focus([[data\],fn])](http://jquery.cuishifeng.cn/focus.html)
  - [focusin([data\],fn)](http://jquery.cuishifeng.cn/focusin.html)
  - [focusout([data\],fn)](http://jquery.cuishifeng.cn/focusout.html)
  - [keydown([[data\],fn])](http://jquery.cuishifeng.cn/keydown.html)
  - [keypress([[data\],fn])](http://jquery.cuishifeng.cn/keypress.html)
  - [keyup([[data\],fn])](http://jquery.cuishifeng.cn/keyup.html)
  - [mousedown([[data\],fn])](http://jquery.cuishifeng.cn/mousedown.html)
  - [mouseenter([[data\],fn])](http://jquery.cuishifeng.cn/mouseenter.html)
  - [mouseleave([[data\],fn])](http://jquery.cuishifeng.cn/mouseleave.html)
  - [mousemove([[data\],fn])](http://jquery.cuishifeng.cn/mousemove.html)
  - [mouseout([[data\],fn])](http://jquery.cuishifeng.cn/mouseout.html)
  - [mouseover([[data\],fn])](http://jquery.cuishifeng.cn/mouseover.html)
  - [mouseup([[data\],fn])](http://jquery.cuishifeng.cn/mouseup.html)
  - [resize([[data\],fn])](http://jquery.cuishifeng.cn/resize.html)
  - [scroll([[data\],fn])](http://jquery.cuishifeng.cn/scroll.html)
  - [select([[data\],fn])](http://jquery.cuishifeng.cn/select.html)
  - [submit([[data\],fn])](http://jquery.cuishifeng.cn/submit.html)
  - ~~unload([[data],fn])~~1.8-

## 效果

- ### 基本

  - [show([s,[e\],[fn]])](http://jquery.cuishifeng.cn/show.html)
  - [hide([s,[e\],[fn]])](http://jquery.cuishifeng.cn/hide.html)
  - [toggle([s\],[e],[fn])](http://jquery.cuishifeng.cn/toggle.html)

- ### 滑动

  - [slideDown([s\],[e],[fn])](http://jquery.cuishifeng.cn/slideDown.html)
  - [slideUp([s,[e\],[fn]])](http://jquery.cuishifeng.cn/slideUp.html)
  - [slideToggle([s\],[e],[fn])](http://jquery.cuishifeng.cn/slideToggle.html)

- ### 淡入淡出

  - [fadeIn([s\],[e],[fn])](http://jquery.cuishifeng.cn/fadeIn.html)
  - [fadeOut([s\],[e],[fn])](http://jquery.cuishifeng.cn/fadeOut.html)
  - [fadeTo([[s\],o,[e],[fn]])](http://jquery.cuishifeng.cn/fadeTo.html)
  - [fadeToggle([s,[e\],[fn]])](http://jquery.cuishifeng.cn/fadeToggle.html)

- ### 自定义

  - [animate(p,[s\],[e],[fn])](http://jquery.cuishifeng.cn/animate.html)1.8*
  - [stop([c\],[j])](http://jquery.cuishifeng.cn/stop.html)1.7*
  - [delay(d,[q\])](http://jquery.cuishifeng.cn/delay.html)
  - [finish([queue\])](http://jquery.cuishifeng.cn/finish.html)1.9+

- ### 设置

  - [jQuery.fx.off](http://jquery.cuishifeng.cn/jQuery.fx.off.html)
  - ~~jQuery.fx.interval~~3.0-

## 工具

- ### 浏览器及特性检测

  - ~~$.support~~1.9-
  - ~~$.browser~~1.9-
  - [$.browser.version](http://jquery.cuishifeng.cn/jQuery.browser.version.html)
  - ~~$.boxModel~~

- ### 数组和对象操作

  - [$.each(object,[callback\])](http://jquery.cuishifeng.cn/jQuery.each.html)
  - [$.extend([d\],tgt,obj1,[objN])](http://jquery.cuishifeng.cn/jQuery.extend.html)
  - [$.grep(array,fn,[invert\])](http://jquery.cuishifeng.cn/jQuery.grep.html)
  - ~~$.sub()~~1.9-
  - [$.when(deferreds)](http://jquery.cuishifeng.cn/jQuery.when.html)
  - [$.makeArray(obj)](http://jquery.cuishifeng.cn/jQuery.makeArray.html)
  - [$.map(arr|obj,callback)](http://jquery.cuishifeng.cn/jQuery.map.html)
  - [$.inArray(val,arr,[from\])](http://jquery.cuishifeng.cn/jQuery.inArray.html)
  - [$.toArray()](http://jquery.cuishifeng.cn/jQuery.toArray.html)
  - [$.merge(first,second)](http://jquery.cuishifeng.cn/jQuery.merge.html)
  - ~~$.unique(array)~~3.0-
  - [$.uniqueSort(array)](http://jquery.cuishifeng.cn/jQuery.uniqueSort.html)3.0+
  - ~~$.parseJSON(json)~~3.0-
  - [$.parseXML(data)](http://jquery.cuishifeng.cn/jQuery.parseXML.html)

- ### 函数操作

  - [$.noop](http://jquery.cuishifeng.cn/jQuery.noop.html)
  - [$.proxy(function,context)](http://jquery.cuishifeng.cn/jQuery.proxy.html)

- ### 测试操作

  - [$.contains(c,c)](http://jquery.cuishifeng.cn/jQuery.contains.html)
  - [$.type(obj)](http://jquery.cuishifeng.cn/jQuery.type.html)
  - ~~$.isArray(obj)~~3.2-
  - ~~$.isFunction(obj)~~3.3-
  - [$.isEmptyObject(obj)](http://jquery.cuishifeng.cn/jQuery.isEmptyObject.html)
  - [$.isPlainObject(obj)](http://jquery.cuishifeng.cn/jQuery.isPlainObject.html)
  - ~~$.isWindow(obj)~~3.3-
  - [$.isNumeric(value)](http://jquery.cuishifeng.cn/jQuery.isNumeric.html)1.7+

- ### 字符串操作

  - [$.trim(str)](http://jquery.cuishifeng.cn/jQuery.trim.html)

- ### URL

  - [$.param(obj,[traditional\])](http://jquery.cuishifeng.cn/jQuery.param.html)

- ### 插件编写

  - [$.error(message)](http://jquery.cuishifeng.cn/jQuery.error.html)
  - [$.fn.jquery](http://jquery.cuishifeng.cn/jquery.html)

## 筛选

- ### 过滤

  - [eq(index|-index)](http://jquery.cuishifeng.cn/eq.html)
  - [first()](http://jquery.cuishifeng.cn/first.html)
  - [last()](http://jquery.cuishifeng.cn/last.html)
  - [hasClass(class)](http://jquery.cuishifeng.cn/hasClass.html)
  - [filter(expr|obj|ele|fn)](http://jquery.cuishifeng.cn/filter.html)
  - [is(expr|obj|ele|fn)](http://jquery.cuishifeng.cn/is.html)
  - [map(callback)](http://jquery.cuishifeng.cn/map.html)
  - [has(expr|ele)](http://jquery.cuishifeng.cn/has.html)
  - [not(expr|ele|fn)](http://jquery.cuishifeng.cn/not.html)
  - [slice(start,[end\])](http://jquery.cuishifeng.cn/slice.html)

- ### 查找

  - [children([expr\])](http://jquery.cuishifeng.cn/children.html)
  - [closest(e|o|e)](http://jquery.cuishifeng.cn/closest.html)1.7*
  - [find(e|o|e)](http://jquery.cuishifeng.cn/find.html)
  - [next([expr\])](http://jquery.cuishifeng.cn/next.html)
  - [nextAll([expr\])](http://jquery.cuishifeng.cn/nextAll.html)
  - [nextUntil([e|e\][,f])](http://jquery.cuishifeng.cn/nextUntil.html)
  - [offsetParent()](http://jquery.cuishifeng.cn/offsetParent.html)
  - [parent([expr\])](http://jquery.cuishifeng.cn/parent.html)
  - [parents([expr\])](http://jquery.cuishifeng.cn/parents.html)
  - [parentsUntil([e|e\][,f])](http://jquery.cuishifeng.cn/parentsUntil.html)
  - [prev([expr\])](http://jquery.cuishifeng.cn/prev.html)
  - [prevAll([expr\])](http://jquery.cuishifeng.cn/prevAll.html)
  - [prevUntil([e|e\][,f])](http://jquery.cuishifeng.cn/prevUntil.html)
  - [siblings([expr\])](http://jquery.cuishifeng.cn/siblings.html)

- ### 串联

  - [add(e|e|h|o[,c\])](http://jquery.cuishifeng.cn/add.html)1.9*
  - ~~andSelf()~~1.8-
  - [addBack()](http://jquery.cuishifeng.cn/addBack.html)1.9+
  - [contents()](http://jquery.cuishifeng.cn/contents.html)
  - [end()](http://jquery.cuishifeng.cn/end.html)

## 事件对象

- [eve.currentTarget](http://jquery.cuishifeng.cn/event.currentTarget.html)
- [eve.data](http://jquery.cuishifeng.cn/event.data.html)
- [eve.delegateTarget](http://jquery.cuishifeng.cn/event.delegateTarget.html)1.7+
- [eve.isDefaultPrevented()](http://jquery.cuishifeng.cn/event.isDefaultPrevented.html)
- [eve.isImmediatePropag...()](http://jquery.cuishifeng.cn/event.isImmediatePropagationStopped.html)
- [eve.isPropagationStopped()](http://jquery.cuishifeng.cn/event.isPropagationStopped.html)
- [eve.namespace](http://jquery.cuishifeng.cn/event.namespace.html)
- [eve.pageX](http://jquery.cuishifeng.cn/event.pageX.html)
- [eve.pageY](http://jquery.cuishifeng.cn/event.pageY.html)
- [eve.preventDefault()](http://jquery.cuishifeng.cn/event.preventDefault.html)
- [eve.relatedTarget](http://jquery.cuishifeng.cn/event.relatedTarget.html)
- [eve.result](http://jquery.cuishifeng.cn/event.result.html)
- [eve.stopImmediatePro...()](http://jquery.cuishifeng.cn/event.stopImmediatePropagation.html)
- [eve.stopPropagation()](http://jquery.cuishifeng.cn/event.stopPropagation.html)
- [eve.target](http://jquery.cuishifeng.cn/event.target.html)
- [eve.timeStamp](http://jquery.cuishifeng.cn/event.timeStamp.html)
- [eve.type](http://jquery.cuishifeng.cn/event.type.html)
- [eve.which](http://jquery.cuishifeng.cn/event.which.html)

## 延迟对象

- [def.done(d,[d\])](http://jquery.cuishifeng.cn/deferred.done.html)
- [def.fail(failCallbacks)](http://jquery.cuishifeng.cn/deferred.fail.html)
- ~~def.isRejected()~~1.7-
- ~~def.isResolved()~~1.7-
- [def.reject(args)](http://jquery.cuishifeng.cn/deferred.reject.html)
- [def.rejectWith(c,[a\])](http://jquery.cuishifeng.cn/deferred.rejectWith.html)
- [def.resolve(args)](http://jquery.cuishifeng.cn/deferred.resolve.html)
- [def.resolveWith(c,[a\])](http://jquery.cuishifeng.cn/deferred.resolveWith.html)
- ~~def.then(d[,f][,p])~~1.8*
- [def.promise([ty\],[ta])](http://jquery.cuishifeng.cn/deferred.promise.html)
- ~~def.pipe([d],[f],[p])~~1.8-
- [def.always(al,[al\])](http://jquery.cuishifeng.cn/deferred.always.html)
- [def.notify(args)](http://jquery.cuishifeng.cn/deferred.notify.html)1.7+
- [def.notifyWith(c,[a\])](http://jquery.cuishifeng.cn/deferred.notifyWith.html)1.7+
- [def.progress(proCal)](http://jquery.cuishifeng.cn/deferred.progress.html)1.7+
- [def.state()](http://jquery.cuishifeng.cn/deferred.state.html)1.7+

## 回调函数

- [cal.add(callbacks)](http://jquery.cuishifeng.cn/callbacks.add.html)1.7+
- [cal.disable()](http://jquery.cuishifeng.cn/callbacks.disable.html)1.7+
- [cal.empty()](http://jquery.cuishifeng.cn/callbacks.empty.html)1.7+
- [cal.fire(arguments)](http://jquery.cuishifeng.cn/callbacks.fire.html)1.7+
- [cal.fired()](http://jquery.cuishifeng.cn/callbacks.fired.html)1.7+
- [cal.fireWith([c\] [,a])](http://jquery.cuishifeng.cn/callbacks.fireWith.html)1.7+
- [cal.has(callback)](http://jquery.cuishifeng.cn/callbacks.has.html)1.7+
- [cal.lock()](http://jquery.cuishifeng.cn/callbacks.lock.html)1.7+
- [cal.locked()](http://jquery.cuishifeng.cn/callbacks.locked.html)1.7+
- [cal.remove(callbacks)](http://jquery.cuishifeng.cn/callbacks.remove.html)1.7+
- [$.callbacks(flags)](http://jquery.cuishifeng.cn/jQuery.callbacks.html)1.7+

## 其它

- [正则表达式](http://jquery.cuishifeng.cn/regexp.html)
- [HTML5速查表](http://jquery.cuishifeng.cn/html5.html)
- [源码下载](http://jquery.cuishifeng.cn/source.html)
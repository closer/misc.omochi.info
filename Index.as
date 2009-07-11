package {
	
	import flash.display.*;
	import flash.text.*;
	import flash.external.*;
	
	public class Index extends Sprite {
		
		private var text_field:TextField;
		private var count:int;
		
		public function Index () {
			text_field = new TextField();
			addChild(text_field);
			ExternalInterface.addCallback('setString', setString);
			count = 0;
		}
		
		public function setString(text:String):String {
			text_field.text = count.toString() + text || "TEST";
			count++;
			return text_field.text;
		}
	}
}
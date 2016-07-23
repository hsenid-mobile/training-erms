
(function(window, document, $){


$(document).on( 'init.dt.dth', function (e, settings, json) {
	var table = new $.fn.dataTable.Api( settings );
	var body = $( table.table().body() );

	if (
		$( table.table().node() ).hasClass( 'searchHighlight' ) || // table has class
		settings.oInit.searchHighlight                          || // option specified
		$.fn.dataTable.defaults.searchHighlight                    // default set
	) {
		table
			.on( 'draw.dt.dth column-visibility.dt.dth', function () {
				// On each draw highlight search results, removing the old ones
				body.unhighlight();

				// Don't highlight the "not found" row
				if ( table.rows( { filter: 'applied' } ).data().length ) {
					body.highlight( table.search().split(' ') );
				}
			} )
			.on( 'destroy', function () {
				table.off( 'draw.dt.dth column-visibility.dt.dth' );
			} );
	}
} );


})(window, document, jQuery);

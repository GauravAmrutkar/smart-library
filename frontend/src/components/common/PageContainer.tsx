import Box from "@mui/material/Box";

import type { ReactNode } from "react";

type PageContainerProps = {
  children: ReactNode;
};

const PageContainer = ({
  children,
}: PageContainerProps) => {
  return (
    <Box
      sx={{
        p: {
          xs: 2,
          md: 3,
        },
      }}
    >
      {children}
    </Box>
  );
};

export default PageContainer;